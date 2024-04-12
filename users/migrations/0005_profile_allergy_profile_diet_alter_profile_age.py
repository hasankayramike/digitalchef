# Generated by Django 4.2.8 on 2024-01-03 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_alter_profile_age"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="allergy",
            field=models.CharField(default="", max_length=20),
        ),
        migrations.AddField(
            model_name="profile",
            name="diet",
            field=models.CharField(default="anything", max_length=20),
        ),
        migrations.AlterField(
            model_name="profile", name="age", field=models.IntegerField(default=0),
        ),
    ]
