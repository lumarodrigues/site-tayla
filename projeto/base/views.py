from django.shortcuts import render

from django.views.generic import ListView

from .models import Upload


class Home(ListView):
    model = Upload
    template_name = 'base/home.html'


def home(request):
    return render(request, 'base/home.html')

