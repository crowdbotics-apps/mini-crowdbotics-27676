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
