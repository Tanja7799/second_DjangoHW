from django.db import models
from django.utils.text import slugify

class Car(models.Model):

    FUEL_CHOICES = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric')
    ]

    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True)
    country = models.CharField(max_length=100)
    body = models.TextField()
    pover = models.IntegerField()
    fuel_type = models.CharField(max_length=50, choices=FUEL_CHOICES)
    is_available = models.BooleanField(default=True)


    # class Meta:
    #      verbose_name = 'Автомобіль'
    #      verbose_name_plural = 'Автомобілі'
    #
    #
    #     def __str__(self):
    #         return self.make