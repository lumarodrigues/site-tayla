from django.views.generic import ListView

from .models import Upload


class HomePageView(ListView):
    model = Upload
    template_name = 'base/home.html'

