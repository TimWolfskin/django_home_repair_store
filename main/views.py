from django.shortcuts import render
from django.http import HttpResponse

from products.models import Categories


def index(request):

    context = {
        'title': 'Home',
        'content': 'This is a main page',
    }

    return render(request, 'main/index.html', context)