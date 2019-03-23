from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Restaurant(models.Model):
    restaurantName = models.CharField(max_length=50)
    restaurantCity = models.CharField(max_length=10)
    restaurantCusine = models.CharField(max_length=10)
    restaurantCostForTwo = models.CharField(max_length=10)
    restaurantRating = models.CharField(max_length=10)
    restaurantRatingText = 	models.CharField(max_length=100)
    restaurantRatingColor	= models.CharField(max_length=10)
    restaurantRatingVotes	= models.CharField(max_length=10)
    restaurantImage = models.URLField()

    def __str__(self):
        return self.restaurantName

class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    birth_date = models.DateField()
    location = models.CharField(max_length=100, blank=True)

# class Person(models.Model):
#     restaurant_id = models.
#     review = models.EmailField(blank=True)
#     birth_date = models.DateField()
#     location = models.CharField(max_length=100, blank=True)
