from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def calculator(request):
    return HttpResponse(request, "Hello, try Calculator")


def add(request, value1, value2):

    suma = int(value1) + int(value2)
    return render(
     request,
     'add.html',
     context={
         "value1": value1,
         "value2": value2,
         "suma": suma

     })

def substract(request, value1, value2):
    subs_result = int(value1) - int(value2)
    return render(
         request,
         'substract.html',
         context={
             "value1": value1,
             "value2": value2,
             "subs_result": subs_result
         })

def multiply(request, value1, value2):
    multi_result =int(value1) * int(value2)
    return render(
         request,
         'multiply.html',
         context={
             "value1": value1,
             "value2": value2,
             "multi_result": multi_result
         })

def divide(request, value1, value2):
    div_result = int(value1) / int(value2)
    return render(
         request,
         'divide.html',
         context={
             "value1": value1,
             "value2": value2,
             "div_result": div_result
         })

