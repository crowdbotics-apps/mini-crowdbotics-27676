import os
import sys
import pytest

from .factories import AppFactory, PlanFactory, SubscriptionFactory
from users.tests.factories import UserFactory


sys.path.append(os.path.dirname(__file__))


@pytest.fixture
def user():
    return UserFactory.create()


@pytest.fixture
def app(user):
    return AppFactory(user=user)


@pytest.fixture
def plan():
    return PlanFactory.create()


@pytest.fixture
def subscription(app, plan, user):
    return SubscriptionFactory(
        app=app,
        plan=plan,
        user=user
    )
