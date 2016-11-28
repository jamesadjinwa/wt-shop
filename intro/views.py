from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .models import ContactForm

# Create your views here.


def intro(request):

    return render(request, 'intro/index.html', {})


def contact(request):

    if request.method == 'GET':

        form_class = ContactForm()

    else:

        form_class = ContactForm(request.POST)

        if form_class.is_valid():
            try:
                from_email = form_class.cleaned_data['contact_email']
                message = form_class.cleaned_data['contact_message']
                # send_mail(subject='Test', message=message, from_email=from_email, recipient_list=['admin@example.com'])
                print(from_email, message)
                # return redirect('/')
            except:
                pass

    return render(request, 'intro/index.html/#contact', {
        'form': form_class,
    })
