from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=100)
    def __str__(self):
        return self.category

class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default='Unknown Category')
    Course_Name = models.CharField(max_length=100)
    def __str__(self):
        return self.Course_Name