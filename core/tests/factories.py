from factory.django import DjangoModelFactory
from core.models.platform import App


class AppFactory(DjangoModelFactory):
    name = "name"
    description = "description"
    type = "Web"
    framework = "Django"
    domain_name = "yourdomain"
    screenshot = "http://example.com"

    class Meta:
        model = App
