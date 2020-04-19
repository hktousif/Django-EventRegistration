from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class RegistrationModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    College_Name = models.CharField(max_length=30)
    Team_Name = models.CharField(max_length=30)
    Place = models.CharField(max_length=30)
    College_Email_ID = models.EmailField(max_length=30)
    Mob_No = models.BigIntegerField()
