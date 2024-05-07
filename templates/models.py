from django.db import models
from django.contrib.auth.models import *
# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=50, blank=True)
    fname = models.CharField(max_length=50, blank=True)
    lname = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    pfp = models.ImageField(upload_to='Astral/templates/files/pfp', blank=True)
    originalName = models.CharField(max_length=50)
