from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def calculator(request):
    return HttpResponse(request, "Hello, try Calculator")


def add(request, value1, value2):
    return render(
         request,
         'add.html',
         context={
             "value1": value1,
             "value2": value2
         })

def substract(request, value1, value2):
    return render(
         request,
         'substract.html',
         context={
             "value1": value1,
             "value2": value2
         })

def multiply(request, value1, value2):
    return render(
         request,
         'multiply.html',
         context={
             "value1": value1,
             "value2": value2
         })

def divide(request, value1, value2):
    return render(
         request,
         'divide.html',
         context={
             "value1": value1,
             "value2": value2
         })

