from django.db import models

# Create your models here.


class Sold(models.Model):
    title = models.CharField(max_length=90)
    ltext = models.CharField(max_length = 20000)
    slug  = models.SlugField(max_length=200)

    date = models.DateTimeField(auto_now_add = True)
