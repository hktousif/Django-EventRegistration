from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# class UserProfileModel(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     Contact_No = models.CharField(max_length=20, blank=True, null=True)
#     Profile_Picture = models.ImageField(upload_to='pics', blank=True, null=True)
#     DOB = models.DateField(blank=True, null=True)
#
#     def __str__(self):
#         return self.user.username
