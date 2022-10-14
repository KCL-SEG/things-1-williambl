from django.db import models

# Create your models here.

class Thing(models.Model):
    name = models.TextField()
    description = models.BigAutoField()
    quantity = models.IntegerField()
