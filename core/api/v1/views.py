from collections import namedtuple

from rest_framework import status
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.models import App, Plan, Subscription, AppTypeChoices, AppFrameWorkChoices
from .serializers import AppSerializer, PlanSerializer, SubscriptionSerializer


AppStack = namedtuple("Stack", "type framework")

web_stack = AppStack(AppTypeChoices.WEB, AppFrameWorkChoices.DJANGO)

mobile_stack = AppStack(AppTypeChoices.MOBILE, AppFrameWorkChoices.REACT_NATIVE)


class AppListCreateAPIView(ListCreateAPIView):
    queryset = App.objects.all().order_by("-created_at")
    permission_classes = (IsAuthenticated,)
    serializer_class = AppSerializer

    def create(self, request, *args, **kwargs):
        """
        Create an App owned by the currenly authenticated user.
        """
        framework = request.data.get("framework")
        type_ = request.data.get("type")

        if (type_ == web_stack.type and framework == web_stack.framework) or (
            type_ == mobile_stack.type and framework == mobile_stack.framework
        ):

            name = request.data.get("name")
            description = request.data.get("description")
            domain_name = request.data.get("domain_name")
            user = request.user
            try:
                app = App.objects.create(
                    name=name,
                    description=description,
                    type=type_,
                    framework=framework,
                    domain_name=domain_name,
                    user=user,
                )
                serializer = self.get_serializer(app)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as exception:
                return Response(
                    {"message": exception.args}, status=status.HTTP_400_BAD_REQUEST
                )
        else:
            try:
                raise ValueError(
                    f"Invalid combination of type and framework. "
                    f"Allowed choices are [{web_stack.type.value},"
                    f" {web_stack.framework.value}] or"
                    f"[{mobile_stack.type}, "
                    f"{mobile_stack.framework.value}]"
                )
            except ValueError as error:
                return Response(
                    {"message": str(error)}, status=status.HTTP_400_BAD_REQUEST
                )


class AppReadUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = App.objects.all().order_by("-created_at")
    permission_classes = (IsAuthenticated,)
    serializer_class = AppSerializer


class PlanListAPIView(ListAPIView):
    queryset = Plan.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = PlanSerializer


class PlanRetrieveAPIView(RetrieveAPIView):
    queryset = Plan.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = PlanSerializer


class SubscriptionRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Subscription.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = SubscriptionSerializer


class SubscriptionListCreateAPIView(ListCreateAPIView):
    queryset = Subscription.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = SubscriptionSerializer

    def create(self, request, *args, **kwargs):
        """
        Create a Subcscription and associate it with an App and a Plan.
        """
        try:
            plan_id = request.data.get("plan")
            app_id = request.data.get("app")
            active = request.data.get("active")
            user = request.user
            subscription = Subscription.objects.create(
                plan_id=plan_id, app_id=app_id, user_id=user.id, active=active
            )
            serializer = self.get_serializer(subscription)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as err:
            return Response({"message": str(err)}, status=status.HTTP_400_BAD_REQUEST)
