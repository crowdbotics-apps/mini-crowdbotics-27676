from decimal import Decimal
import pytest
from .factories import AppFactory, PlanFactory, SubscriptionFactory

pytestmark = pytest.mark.django_db


def test_create_app(user):
    app_payload = dict(
        user=user,
        name="testing_app",
        description="App for testing purposes",
        type="Web",
        framework="Django",
        domain_name="localhost:8000",
        screenshot="http://www.screenshot_example.com",
    )
    app = AppFactory(**app_payload)
    assert app.domain_name == app_payload["domain_name"]


def test_create_standard_plan():
    plan_payload = dict(name="Standard", price=Decimal(10), description="Standard")
    plan = PlanFactory(**plan_payload)
    assert plan.price == plan_payload["price"]
    assert plan.name == plan_payload["name"]


def test_create_subscription(user):
    app_payload = dict(
        user=user,
        name="app_two",
        description="another one",
        type="Mobile",
        framework="React Native",
        domain_name="localhost:3000",
        screenshot="http://www.screenshot_example.com",
    )
    app = AppFactory(**app_payload)
    plan_payload = dict(name="Pro", price=Decimal(25), description="Pro")
    plan = PlanFactory(**plan_payload)
    subscription = SubscriptionFactory(app=app, plan=plan, user=user)
    assert subscription.plan.name == plan_payload["name"]
    assert subscription.plan.price == plan_payload["price"]


def test_delete_subscription(subscription):
    assert subscription.active == True
    subscription.delete()
    assert subscription.active == False
