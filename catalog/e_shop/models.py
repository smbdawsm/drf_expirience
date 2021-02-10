from django.db import models


class Item(models.Model):

    categories = models.ManyToManyField('Category', related_name='Categories')
    price = models.IntegerField(verbose_name='Price')
    name = models.CharField(verbose_name="name", max_length=100)
    description = models.TextField(default='')
    published = models.BooleanField()
    deleted = models.BooleanField()

    def __str__(self):
        return self.name


class Category(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
