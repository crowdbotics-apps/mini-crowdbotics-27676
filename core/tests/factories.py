from decimal import Decimal
from factory.django import DjangoModelFactory
from core.models.platform import App


class AppFactory(DjangoModelFactory):
    name = "name"
    description = "description"
    type = "Mobile"
    framework = "React Native"
    domain_name = "localhost"
    screenshot = "http://mydomainexample.com"

    class Meta:
        model = App


class PlanFactory(DjangoModelFactory):
    name = "Free"
    description = "description"
    price = Decimal(0)

    class Meta:
        model = Plan
