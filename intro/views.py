import pdb
from django.shortcuts import render
from django.core.mail import BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template

# Create your views here.


def intro(request):

    if request.method == 'GET':

        form_class = ContactForm()

    else:

        form_class = ContactForm(request.POST or None, request.FILES or None)

        if form_class.is_valid():

            try:
                contact_name = request.POST.get('contact_name', '')
                contact_email = request.POST.get('contact_email', '')
                message = request.POST.get('contact_message', '')
                phone = form_class.cleaned_data['contact_phone']

                template = get_template('intro/contact_template.txt')
                context = Context({
                    'contact_name': contact_name,
                    'contact_email': contact_email,
                    'phone': phone,
                    'message': message,
                })

                content = template.render(context)
                email = EmailMessage(
                    "New contact form submission",
                    content,
                    "www.wizardstechnology.biz" + '',
                    ['gqkircyu@grr.la'],                            # TODO: change this email on production host
                    headers={'Reply-To': contact_email}
                )

                email.send()
                print(contact_name, contact_email, phone, message)
                messages.success(request, 'Thank you for your message !')

                # pdb.set_trace()
                return HttpResponseRedirect('')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

        # else:
        #     messages.add_message(request, messages.ERROR, 'Sorry ...')
        #     return HttpResponseRedirect('#contact')

    return render(request, 'intro/index.html', {'form': form_class, })

