import datetime
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def is_it_monday(request):
    now = datetime.now()

    is_monday = False
    if now.weekday() == 0:
        is_monday = True

    return render(
        request,
        'is_it_monday.html',
        context={
            'is_monday': is_monday}
    )

    return render(
        request,
        'is_it_monday.html')

