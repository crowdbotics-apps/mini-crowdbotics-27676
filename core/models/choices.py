from django.db import models


class AppTypeChoices(models.TextChoices):
    WEB = "Web", "Web"
    MOBILE = "Mobile", "Mobile"


class AppFrameWorkChoices(models.TextChoices):
    DJANGO = "Django", "Django"
    REACT_NATIVE = "React Native", "React Native"
