import pytest
from django.test import RequestFactory
from users.tests.factories import UserFactory


@pytest.fixture
def user():
    return UserFactory.create()


@pytest.fixture
def request_factory():
    return RequestFactory()
