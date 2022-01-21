from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):

    class Types(models.TextChoices):
        EMPLOYEE = 'EMPLOYEE', 'Employee'
        PLANNER = 'PLANNER', 'Planner'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(_('Type'), max_length=50, choices=Types.choices, default=Types.EMPLOYEE)
    is_merchandizer = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    profile_pic = CloudinaryField('images')
    createdAtDate = models.DateTimeField(auto_now_add=True)
    
    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

class EmployeeManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.EMPLOYEE)

class PlannerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.PLANNER)

class Employee(User):
    objects = EmployeeManager()
    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.EMPLOYEE
        return super().save(*args, **kwargs)

class Planner(User):
    objects = PlannerManager()
    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.PLANNER
        return super().save(*args, **kwargs)

