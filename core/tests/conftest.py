import os
import sys
import pytest

from .factories import AppFactory
from users.tests.factories import UserFactory


sys.path.append(os.path.dirname(__file__))


@pytest.fixture
def user():
    return UserFactory.create()


@pytest.fixture
def app(user):
    return AppFactory(user=user)
