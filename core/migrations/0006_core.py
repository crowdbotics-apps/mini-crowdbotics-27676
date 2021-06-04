# Generated by Django 3.2.4 on 2021-06-04 13:17

from django.db import migrations
from decimal import Decimal


def add_default_plans(apps, schema_editor):
    Plan = apps.get_model("core.Plan")
    plans = [
        {
            "name": "Free",
            "description": "Free",
            "price": Decimal(0),
        },
        {
            "name": "Standard",
            "description": "Standard",
            "price": Decimal(10),
        },
        {
            "name": "Pro",
            "description": "Pro",
            "price": Decimal(25),
        },
    ]
    for plan in plans:
        Plan.objects.create(**plan)


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_core"),
    ]

    operations = [migrations.RunPython(add_default_plans, migrations.RunPython.noop)]
