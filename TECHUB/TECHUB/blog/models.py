from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    stext  = models.CharField(max_length=500)
    slug  = models.SlugField(max_length=200)
    mytext = models.TextField(max_length = 5000)
    date = models.DateTimeField(auto_now_add=True)