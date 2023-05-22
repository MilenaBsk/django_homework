from django.shortcuts import render

# Create your views here.

def toto_lotek(request):
    return render(
        request,
        'toto_lotek.html'
    )