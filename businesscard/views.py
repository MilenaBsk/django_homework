from django.shortcuts import render

# Create your views here.
def businesscard(request):
    return render(
        request,
        'businesscard.html'
    )