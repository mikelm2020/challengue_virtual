# Generated by Django 4.1.4 on 2022-12-19 00:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("hits", "0004_alter_hits_creator"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="hits",
            options={"verbose_name": "Hit", "verbose_name_plural": "Hits"},
        ),
        migrations.AlterField(
            model_name="hits",
            name="creator",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="created_for",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
