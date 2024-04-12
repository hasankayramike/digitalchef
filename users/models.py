from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    diet = models.CharField(default="anything", max_length=20)
    allergy = models.CharField(default="", max_length=20)
    age = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    sex = models.CharField(default="male", max_length=10)
    goal = models.TextField(default="maintain_weight", max_length=20)
    activity = models.TextField(default="sedentary", max_length=20)
    protein = models.IntegerField(default=0)
    carbs = models.IntegerField(default=0)
    fat = models.IntegerField(default=0)
    calories = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} Profile"