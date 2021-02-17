from django.http import HttpResponse
from django.shortcuts import render

from projeto.forms import FormularioForm


def home(request):
    return render(request, 'base/home.html')


def about_me(request):
    return render(request, 'base/about_me.html')


def sketchbook(request):
    return render(request, 'base/sketchbook.html')


def contact_me(request):
    if request.method == "POST":
        form = FormularioForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'base/contact_me.html')
        else:
            return HttpResponse('Formulario Invalido.')
    return render(request, 'base/contact_me.html')
