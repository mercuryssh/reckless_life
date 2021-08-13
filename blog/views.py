#from django.shortcuts import render
from django.http import JsonResponse
from . import models

# Create your views here.
def say_hello(request):
    data = {"message": "Hello world, Mashu here ✌🏻"}
    return JsonResponse(data)