from django.db import models

# Create your models here.

class Info(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    intime=models.DateTimeField()
    outtime=models.DateTimeField(null=True, blank=True)
    msg=models.CharField(max_length=100)