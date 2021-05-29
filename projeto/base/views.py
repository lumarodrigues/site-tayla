from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from projeto.forms import FormularioForm
from projeto.settings import EMAIL_USER


def home(request):
    return render(request, 'base/home.html')


def about_me(request):
    return render(request, 'base/about_me.html')


def sketchbook(request):
    return render(request, 'base/sketchbook.html')


def thank_you(request):
    template = 'base/thank_you.html'
    context = {}
    return render(request, template, context)


def contact_me(request):
    if request.method == 'POST':
        form = FormularioForm(request.POST)
        name = request.POST['nome']
        email = request.POST['email']
        message = request.POST['mensagem']

        try:
            send_mail('Mensagem de ' + name, 'Nome: ' + name + '\nEmail: ' + email + '\n\nMensagem: ' + message,
                      [EMAIL_USER], [EMAIL_USER], fail_silently=False,)
            return redirect('/thank_you/')
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
    return render(request, 'base/contact_me.html')
