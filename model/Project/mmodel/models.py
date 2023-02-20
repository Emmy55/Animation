from django.db import models

# Create your models here.

class Pan(models.Model):
    # id = model.CharField(max_length = 200)
    num = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    des = models.CharField(max_length=300)