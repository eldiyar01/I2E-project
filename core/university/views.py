from django.shortcuts import render
from .models import University


def home(request):
    universities = University.objects.all()
    return render(request, 'university/home.html', {'universities': universities})
