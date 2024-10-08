from django.shortcuts import render
from django.http import HttpResponse

from products.models import Categories


def index(request):
    categories = Categories.objects.all()
    context = {
        'title': 'Home',
        'content': 'This is a main page',
        'categories': categories
    }

    return render(request, 'main/index.html', context)