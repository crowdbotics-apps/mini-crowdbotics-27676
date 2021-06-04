from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.models import App
from .serializers import AppSerializer


class AppListCreateAPIView(ListCreateAPIView):
    queryset = App.objects.all().order_by("-created_at")
    permission_classes = (IsAuthenticated,)
    serializer_class = AppSerializer

    def create(self, request, *args, **kwargs):
        name = request.data.get("name")
        description = request.data.get("description")
        type_ = request.data.get("type")
        framework = request.data.get("framework")
        domain_name = request.data.get("domain_name")
        user = request.user
        try:
            app = App.objects.create(
                name=name,
                description=description,
                type=type_,
                framework=framework,
                domain_name=domain_name,
                user=user
            )
            serializer = self.get_serializer(app)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as exception:
            return Response(
                {"message": exception.args},
                status=status.HTTP_400_BAD_REQUEST
            )
