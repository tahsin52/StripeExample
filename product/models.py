from django.db import models
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10, default=39.99)
    active = models.BooleanField(default=True)
    is_digital = models.BooleanField(default=False) # User Library

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    @property
    def name(self):
        return self.title

