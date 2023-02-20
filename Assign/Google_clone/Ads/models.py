from django.db import models

# Create your models here.



# class mode:
#     id : int
#     title: str
#     des: str


class mode(models.Model):
    num = models.CharField(max_length=30)
    title = models.CharField(max_length=300)
    des = models.CharField(max_length=30)