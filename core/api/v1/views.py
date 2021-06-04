from rest_framework import status
from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.models import App, Plan, Subscription, AppTypeChoices,\
    AppFrameWorkChoices
from .serializers import AppSerializer, PlanSerializer, SubscriptionSerializer


class AppListCreateAPIView(ListCreateAPIView):
    queryset = App.objects.all().order_by("-created_at")
    permission_classes = (IsAuthenticated,)
    serializer_class = AppSerializer

    def create(self, request, *args, **kwargs):
        name = request.data.get("name")
        description = request.data.get("description")
        type_ = request.data.get("type")
        domain_name = request.data.get("domain_name")
        user = request.user
        framework = request.data.get("framework")
        try:
            if type_ not in AppTypeChoices:
                raise ValueError("Type must be one of: Web, Mobile")
            if framework not in AppFrameWorkChoices:
                raise ValueError("Framework must be one of: "
                                 "Django, React Native")
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


class SubscriptionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Subscription.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = SubscriptionSerializer

    def destroy(self, request, *args, **kwargs):
        subscription_id = kwargs.get("pk")
        subscription = Subscription.objects.get(id=subscription_id)
        subscription.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SubscriptionListCreateAPIView(ListCreateAPIView):
    queryset = Subscription.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = SubscriptionSerializer

    def create(self, request, *args, **kwargs):
        plan_id = request.data.get("plan")
        app_id = request.data.get("app")
        active = request.data.get("active")
        user = request.user
        subscription = Subscription.objects.create(
            plan_id=plan_id,
            app_id=app_id,
            user_id=user.id,
            active=active
        )
        serializer = self.get_serializer(subscription)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
