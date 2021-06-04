import os
import sys
import pytest
from rest_framework.test import APIRequestFactory

from .factories import AppFactory, PlanFactory, SubscriptionFactory
from users.tests.factories import UserFactory
from ..api.v1.views import AppListCreateAPIView, PlanListAPIView, \
    PlanRetrieveAPIView, SubscriptionRetrieveUpdateDestroyAPIView, \
    SubscriptionListCreateAPIView

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


@pytest.fixture
def app_list_create_view():
    return AppListCreateAPIView.as_view()


@pytest.fixture
def api_request_factory():
    return APIRequestFactory()


@pytest.fixture
def plan_list_view():
    return PlanListAPIView.as_view()


@pytest.fixture
def plan_retrieve_view():
    return PlanRetrieveAPIView.as_view()


@pytest.fixture
def subscription_retrieve_update_destroy_view():
    return SubscriptionRetrieveUpdateDestroyAPIView.as_view()


@pytest.fixture
def subscription_list_create_view():
    return SubscriptionListCreateAPIView.as_view()
