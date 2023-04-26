from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def calculator(request):
   return HttpResponse("Hello calc!")
