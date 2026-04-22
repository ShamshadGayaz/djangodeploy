from django.shortcuts import render
from .models import HomeContent


def home(request):
    contents = HomeContent.objects.filter(is_active=True)
    return render(request, 'myapp/home.html', {'contents': contents})
