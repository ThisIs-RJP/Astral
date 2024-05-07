from django.db import models
from django.contrib.auth.models import *
# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=50, blank=True)
    fname = models.CharField(max_length=50, blank=True)
    lname = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    originalName = models.CharField(max_length=50)

class UserIcon(models.Model):
    originalName = models.CharField(max_length=50)
    pfp = models.ImageField(upload_to='static/images/icons', blank=True, default="static/images/pfp.png")
