from django.db import models


# Create your models here.
class CoordinatorsModel(models.Model):
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    Mob_No = models.BigIntegerField()
    temp = models.CharField(max_length=30)


class ProtocolsModel(models.Model):
    protocol = models.TextField()


class EventsModel(models.Model):
    Event_Name = models.CharField(max_length=15)
    Event_Protocols = models.TextField()
    Event_Poster = models.ImageField(upload_to='pics')
    About_Event = models.TextField()


class AboutModel(models.Model):
    About_IBMR = models.TextField()


class GalleryModel(models.Model):
    Image = models.ImageField(upload_to='pics')
    About_Image = models.TextField()


class ContactModel(models.Model):
    Full_Name = models.CharField(max_length=60)
    Contact_No = models.CharField(max_length=12)
    Email_ID = models.EmailField(null=True, blank=True)
    Post = models.CharField(max_length=30)
    DP = models.ImageField(upload_to='pics', null=True, blank=True)


class HomeSlidesModel(models.Model):
    Image = models.ImageField(upload_to='pics')
    About_1 = models.CharField(max_length=100, null=True, blank=True)
    About_2 = models.CharField(max_length=100, null=True, blank=True)
    About_3 = models.CharField(max_length=100, null=True, blank=True)
