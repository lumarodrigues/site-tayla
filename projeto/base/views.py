from django.shortcuts import render
from projeto.forms import ContactForm
from django.core.mail import send_mail


def home(request):
    return render(request, 'base/home.html')


def about_me(request):
    return render(request, 'base/about_me.html')


def sketchbook(request):
    return render(request, 'base/sketchbook.html')


def contact_me(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail('', message, email, ['rdsluma@gmail.com', email])
    return render(request, 'base/contact_me.html', {'form': form})
