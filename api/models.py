from django.db import models
import os

def get_image_path(instance, filename):
    return os.path.join('images', str(instance.id), filename)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name
