from decimal import Decimal
import pytest
from .factories import AppFactory, PlanFactory

pytestmark = pytest.mark.django_db


def test_create_app(user):
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


def test_create_standard_plan():
    plan_payload = dict(
        name="Standard",
        price=Decimal(10),
        description="Standard"
    )
    plan = PlanFactory(**plan_payload)
    assert plan.price == plan_payload["price"]
    assert plan.name == plan_payload["name"]
