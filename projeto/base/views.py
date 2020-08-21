from django.shortcuts import render

from django.http import HttpResponse

from django.views.generic import ListView

from .models import Upload


def home(request):
    return render(request, 'base/home.html')


class HomePageView(ListView):
    model = Upload
    template_name = 'home.html'
