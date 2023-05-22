import random

from django.shortcuts import render

# Create your views here.

def toto_lotek(request):
    random_num = random.randint(1, 49)


    return render(
        request,
        'toto_lotek.html',
        context={
            'random_num': random_num

    }
    )


    return render(request, 'random_number.html', {'random_num': random_num})