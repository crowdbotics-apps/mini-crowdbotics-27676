from django.urls import path

from core.api.v1.views import AppListCreateAPIView

urlpatterns = [
    path(
        route='apps/',
        view=AppListCreateAPIView.as_view(),
        name='apps_rest_api'
    )
]
