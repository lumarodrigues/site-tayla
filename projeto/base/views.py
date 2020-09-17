from django.shortcuts import render


def home(request):
    return render(request, 'base/home.html')


def about_me(request):
    return render(request, 'base/about_me.html')


def sketchbook(request):
    return render(request, 'base/sketchbook.html')


def contact_me(request):
    return render(request, 'base/contact_me.html')
