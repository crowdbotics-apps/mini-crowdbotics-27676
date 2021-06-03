import pytest
from django.test import TestCase
from .factories import AppFactory

# Create your tests here.
pytestmark = pytest.mark.django_db


def test_app_create(user):
    app_payload = dict(
        user=user,
        name="testing_app",
        description="App for testing purposes",
        type="Web",
        framework="Django",
        domain_name="localhost:8000",
        screenshot="http://www.screenshot_example.com"
    )
    app = AppFactory(**app_payload)
    assert app.domain_name == app_payload["domain_name"]
