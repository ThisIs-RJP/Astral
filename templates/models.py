from django.db import models
# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField()
    pfp = models.ImageField(upload_to='templates/files/pfp')
