from django.contrib.auth.models import Permission
from django.shortcuts import render,HttpResponse
from django.http import Http404
from rest_framework import status,generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *


def index(request):
    return render(request, 'index.html')