from operator import truediv
from django.db import models

# Create your models here.
class Routes(models.Model):
    manager = models.EmailField(max_length=255)
    slug = models.SlugField(unique=True )
    address = models.CharField(max_length=255)
    