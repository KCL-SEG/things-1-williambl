from django.db import models
from django.core import validators

# Create your models here.

class Thing(models.Model):
    name = models.SlugField(unique=True,validators=[validators.MinLengthValidator(1), validators.MaxLengthValidator(30)])
    description = models.TextField(validators=[validators.MaxLengthValidator(120)])
    quantity = models.IntegerField(validators=[validators.MinValueValidator(0), validators.MaxValueValidator(100)])
