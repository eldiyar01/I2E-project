from django.shortcuts import render, redirect
from .models import University


def home(request):
    universities = University.objects.all()
    return render(request, 'university/home.html', {'universities': universities})


def university_dtl(request, pk):
    university = University.objects.get(id=pk)
    return render(request, 'university/details.html', {'university': university})


def search_result(request):
    search_req = request.GET.get('search')
    if search_req == '':
        return redirect('university:home')
    elif search_req:
        search_univ = University.objects.filter(title__icontains=search_req)
    return render(request, 'university/search_res.html', {'search_univ': search_univ, 'search_req': search_req})
