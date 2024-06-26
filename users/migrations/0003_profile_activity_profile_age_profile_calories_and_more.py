# Generated by Django 4.2.8 on 2024-01-03 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_remove_profile_activity_remove_profile_age_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="activity",
            field=models.TextField(default="sedentary", max_length=20),
        ),
        migrations.AddField(
            model_name="profile", name="age", field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="profile", name="calories", field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="profile", name="carbs", field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="profile", name="fat", field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="profile",
            name="goal",
            field=models.TextField(default="maintain_weight", max_length=20),
        ),
        migrations.AddField(
            model_name="profile", name="height", field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="profile", name="protein", field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="profile",
            name="sex",
            field=models.CharField(default="male", max_length=10),
        ),
        migrations.AddField(
            model_name="profile", name="weight", field=models.IntegerField(default=0),
        ),
    ]
