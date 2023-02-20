from django.db import models

from taggit.managers import TaggableManager

# Create your models here.


class Post(models.Model):
    title = models.Charfield(max_length=250)
    description = models.TextField()
    published = models.DataField(auto_now_add=True)
    slug = models.SlungField(unique=True, max_length=100)
    tags = TaggleManager()

    def __st__(self):
        return self.title