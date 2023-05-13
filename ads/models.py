from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=200)
    is_published = models.BooleanField()
    price = models.PositiveIntegerField()


class Category(models.Model):
    name = models.CharField(max_length=200)



