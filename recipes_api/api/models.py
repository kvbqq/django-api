from django.db import models

# Create your models here.

class Recipes(models.Model):
    host = models.CharField(max_length=50, unique=True)