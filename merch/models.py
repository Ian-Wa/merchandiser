from django.db import models
from cloudinary.models import CloudinaryField
from django.forms import CharField

# Create your models here.
class Merchandizer(models.Model):
    merchandizerId = models.AutoField(primary_key= True)
    userName = models.CharField(max_length=50)
    firstName = models.CharField(max_length= 50)
    lastName = models.CharField(max_length=50)
    emailAddress = models.EmailField(max_length= 100)
    idNo = models.IntegerField()
    profile_pic = CloudinaryField('images')
    createdAtDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.userName

class Manager(models.Model):
    managerId = models.AutoField(primary_key= True)
    userName = models.CharField(max_length=50)
    firstName = models.CharField(max_length= 50)
    lastName = models.CharField(max_length=50)
    routes = models.TextField(max_length=150)
    profile_pic = CloudinaryField('images')

    def __str__(self):
        return self.userName

class Route(models.Model):
    routeId = models.AutoField(primary_key=True)
    route = CharField(max_length=80)

    def __str__(self):
        return self.use