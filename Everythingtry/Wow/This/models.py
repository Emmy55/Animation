from django.db import models

# Create your models here.

class now(models.Model):
    nam = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    des = models.CharField(max_length=20)
    body = models.CharField(max_length=20)


    