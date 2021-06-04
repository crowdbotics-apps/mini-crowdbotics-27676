from decimal import Decimal
import pytest
from rest_framework.test import force_authenticate

from users.tests.factories import UserFactory

from core.tests.factories import AppFactory, PlanFactory, \
    SubscriptionFactory


pytestmark = pytest.mark.django_db


def test_post_app(user, api_request_factory, app_list_create_view):
    app_payload = {
        "name": "zing",
        "description": "zing",
        "type": "Web",
        "framework": "Django"
    }
    request = api_request_factory.post(
        "/api/v1/apps/",
        app_payload
    )
    force_authenticate(request, user=user)
    response = app_list_create_view(request)
    assert response.status_code == 201
    assert response.data["name"] == app_payload["name"]
    assert response.data["framework"] == app_payload["framework"]
    assert response.data["type"] == app_payload["type"]


def test_get_apps(app, user, api_request_factory, app_list_create_view):
    request = api_request_factory.get("/api/v1/apps/")
    force_authenticate(request, user=user)
    response = app_list_create_view(request)
    assert response.data[0]["type"] == app.type
    assert response.data[0]["domain_name"] == app.domain_name
    assert response.data[0]["framework"] == app.framework


def test_list_plans(
        user,
        api_request_factory,
        plan_list_view
):
    free_plan = PlanFactory(name="Free", description="free", price=Decimal(0))
    std_plan = PlanFactory(name="Standard", description="standard",
                           price=Decimal(10))
    pro_plan = PlanFactory(name="Pro", description="pro", price=Decimal(25))
    request = api_request_factory.get("/api/v1/plans/")
    force_authenticate(request, user=user)
    response = plan_list_view(request)
    assert len(response.data) == 6


def test_get_plan(
        user,
        api_request_factory,
        plan_retrieve_view,
        plan
):
    request = api_request_factory.get(f"/api/v1/plans/{plan.id}")
    force_authenticate(request, user=user)
    response = plan_retrieve_view(request, pk=plan.id)
    assert response.data["name"] == plan.name
    assert response.data["id"] == plan.id
