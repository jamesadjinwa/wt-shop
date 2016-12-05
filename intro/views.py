from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .models import ContactForm
from django.contrib import messages
'''
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template
'''

# Create your views here.


def intro(request):

    if request.method == 'GET':

        form_class = ContactForm()

    else:

        form_class = ContactForm(request.POST)

        if form_class.is_valid():
            try:
                name = form_class.cleaned_data['contact_name']
                from_email = form_class.cleaned_data['contact_email']
                message = form_class.cleaned_data['contact_message']
                phone = form_class.cleaned_data['contact_phone']
                import pdb;
                pdb.set_trace()
                send_mail(subject='Test', message=message, from_email=from_email, recipient_list=['admin@example.com'])
                print(name, from_email, phone, message)
                messages.add_message(request, messages.SUCCESS, 'Thank you for your message.')
                return HttpResponseRedirect('/')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

    return render(request, 'intro/index.html', {'form': form_class, })


'''
def intro(request):

    if request.method == 'GET':

        form_class = ContactForm()

    else:

        form_class = ContactForm(request.POST)

        if form_class.is_valid():
            try:
                contact_name = request.POST.get('contact_name', '')
                contact_email = request.POST.get('contact_email', '')
                message = request.POST.get('contact_message', '')
                phone = form_class.cleaned_data['contact_phone']

                template = get_template('contact_template.txt')
                context = Context({
                    'contact_name': contact_name,
                    'contact_email': contact_email,
                    'form_content': message,
                })
                content = template.render(context)

                email = EmailMessage(
                    "New contact form submission",
                    content,
                    "Your website" + '',
                    ['youremail@gmail.com'],
                    headers={'Reply-To': contact_email}
                )
                email.send()
                messages.add_message(request, messages.SUCCESS, 'Thank you for your message.')
                return redirect('/')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

    return render(request, 'intro/index.html', {'form': form_class, })
'''

'''
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
'''
