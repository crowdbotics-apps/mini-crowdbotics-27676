from rest_framework import serializers

from core.models import App, AppTypeChoices, AppFrameWorkChoices, Plan, \
    Subscription


class AppSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=50,
        min_length=1,
        required=True
    )
    description = serializers.CharField(allow_blank=True, required=False)
    type = serializers.ChoiceField(
        choices=AppTypeChoices.choices,
        required=True
    )
    framework = serializers.ChoiceField(
        required=True,
        choices=AppFrameWorkChoices.choices
    )
    domain_name = serializers.CharField(
        max_length=50,
        allow_blank=True,
        required=False
    )
    screenshot = serializers.URLField(read_only=True, allow_blank=True)
    subscription = serializers.IntegerField(
        read_only=True,
    )

    class Meta:
        model = App
        fields = ("id", "name", "description", "type", "framework",
                  "domain_name", "screenshot", "subscription", "user",
                  "created_at", "updated_at",
                  )


class PlanSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=20,
        min_length=1,
        required=True
    )
    description = serializers.CharField(min_length=1)
    price = serializers.DecimalField(
        coerce_to_string=True,
        decimal_places=2,
        max_digits=4,
        required=False
    )

    class Meta:
        model = Plan
        fields = ["id", "name", "description", "price", "created_at",
                  "updated_at"]


class SubscriptionSerializer(serializers.ModelSerializer):
    app = serializers.PrimaryKeyRelatedField(
        required=True,
        queryset=App.objects.all()
    )
    plan = serializers.PrimaryKeyRelatedField(
        required=True,
        queryset=Plan.objects.all()
    )
    user = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    active = serializers.BooleanField(required=True)

    class Meta:
        model = Subscription
        fields = [
            "id", "user", "plan", "app", "active", "created_at", "updated_at"
        ]
