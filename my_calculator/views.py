from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def calculator(request):
    return render(request, "first.html")


def add(request):
    return HttpResponse("hello adds ")

                   # return render(
    #     request,
    #     "add.html",
