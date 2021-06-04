from django.urls import path

from core.api.v1.views import AppListCreateAPIView, AppReadUpdateDeleteView

urlpatterns = [
    path(
        route='apps/',
        view=AppListCreateAPIView.as_view(),
        name='apps_rest_api'
    ),
    path(
        'apps/<int:pk>/',
        AppReadUpdateDeleteView.as_view()
    ),
]
