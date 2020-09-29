from django.shortcuts import render
from projeto.forms import ContactForm
from django.core.mail import send_mail
from projeto.settings import EMAIL_HOST_USER


def home(request):
    return render(request, 'base/home.html')


def about_me(request):
    return render(request, 'base/about_me.html')


def sketchbook(request):
    return render(request, 'base/sketchbook.html')


def contact_me(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        send_mail(message_name, message, message_email, [EMAIL_HOST_USER], fail_silently=False)

        return render(request, 'base/contact_me.html', {'message_name': message_name})
    else:
        return render(request, 'base/contact_me.html', {})
