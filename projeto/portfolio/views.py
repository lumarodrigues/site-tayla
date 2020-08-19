from django.shortcuts import render

from django.views.generic import ListView
from .models import Portfolio


class HomePageView(ListView):
    model = Portfolio
    template_name = 'home.html'