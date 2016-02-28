from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Create your models here.
@python_2_unicode_compatible
class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

@python_2_unicode_compatible
class Destination(models.Model):
    # todos: read about data types and possible params/options
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = models.FileField(upload_to='media')
    category = models.ForeignKey(Category)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title