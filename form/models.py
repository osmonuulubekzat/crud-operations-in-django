from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=120)
    type = models.CharField(max_length=120)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name
