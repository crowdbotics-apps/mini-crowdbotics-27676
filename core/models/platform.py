from django.db import models
from django.conf import settings

from core.models.base import TimeStampedModel
from core.models.choices import AppFrameWorkChoices, AppTypeChoices


class App(TimeStampedModel):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    type = models.CharField(max_length=6, choices=AppTypeChoices.choices)
    framework = models.CharField(
        max_length=12,
        choices=AppFrameWorkChoices.choices
    )
    domain_name = models.CharField(max_length=50, null=True)
    screenshot = models.URLField(null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="apps"
    )

