# Generated by Django 4.1.4 on 2022-12-16 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hitmen", "0002_alter_user_description_alter_user_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="description",
            field=models.TextField(
                blank=True, max_length=50, null=True, verbose_name="Description"
            ),
        ),
    ]