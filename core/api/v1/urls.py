from django.urls import path

from core.api.v1.views import (
    AppListCreateAPIView,
    AppReadUpdateDeleteAPIView,
    PlanListAPIView,
    PlanRetrieveAPIView,
    SubscriptionRetrieveUpdateAPIView,
    SubscriptionListCreateAPIView,
)

urlpatterns = [
    path(route="apps/", view=AppListCreateAPIView.as_view(), name="apps_rest_api"),
    path("apps/<int:pk>/", AppReadUpdateDeleteAPIView.as_view()),
    path("plans/", PlanListAPIView.as_view()),
    path("plans/<int:pk>/", PlanRetrieveAPIView.as_view()),
    path("subscriptions/", SubscriptionListCreateAPIView.as_view()),
    path("subscriptions/<int:pk>/", SubscriptionRetrieveUpdateAPIView.as_view()),
]
