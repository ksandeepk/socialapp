from django.db import models

# Create your models here.
class udata(models.Model):
    name=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    marital_status=models.CharField(max_length=50)
    interest_in=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    profile_picture=models.ImageField(upload_to='')

