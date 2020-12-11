from django.shortcuts import render
from .models import University


def home(request):
    universities = University.objects.all()
    return render(request, 'university/home.html', {'universities': universities})


def university_dtl(request, pk):
    university = University.objects.get(id=pk)
    return render(request, 'university/details.html', {'university': university})
