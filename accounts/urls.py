from django.contrib import admin
from django.urls import path
from . import views

from .views import  RegisterView, RetrieveUserView

urlpatterns = [
    path('', views.index, name='index'),
    path('register', RegisterView.as_view()),
    path('me', RetrieveUserView.as_view())
]