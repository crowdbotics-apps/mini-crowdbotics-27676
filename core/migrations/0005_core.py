# Generated by Django 3.2.4 on 2021-06-04 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_core'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='app',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.app'),
        ),
    ]
