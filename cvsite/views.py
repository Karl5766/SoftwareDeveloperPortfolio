from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def projects(request):
    return render(request, 'projects.html')


def contact(request):
    return render(request, 'contact.html')


def work1(request):
    return render(request, 'projects/work1.html')


def work2(request):
    return render(request, 'projects/work2.html')


def project1(request):
    return render(request, 'projects/project1.html')


def project2(request):
    return render(request, 'projects/project2.html')


def project3(request):
    return render(request, 'projects/project3.html')
