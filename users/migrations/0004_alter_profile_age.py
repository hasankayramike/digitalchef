# Generated by Django 4.2.8 on 2024-01-03 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_profile_activity_profile_age_profile_calories_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile", name="age", field=models.IntegerField(),
        ),
    ]
