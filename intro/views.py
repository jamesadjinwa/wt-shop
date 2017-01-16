from .forms import ContactForm
from django.shortcuts import render
from django.core.mail import BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
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
        print(form_class.is_valid())

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
                    "noreply@wizardstechnology.biz" + '',
                    ['test@localhost'],                            # TODO: change this email on production host
                    headers={'Reply-To': contact_email}
                )

                email.send(fail_silently=False)
                print(contact_name, contact_email, phone, message)

                messages.success(request, 'Thank you for your message !')

                new_form = form_class.save(commit=False)
                new_form.contact_name = contact_name
                new_form.contact_email = contact_email
                new_form.contact_phone = phone
                new_form.contact_message = message
                new_form.save()
                form_class.save_m2m()

                # pdb.set_trace()
                return HttpResponseRedirect('')

            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        else:
            return HttpResponse(status=400)

        # else:
        #     messages.add_message(request, messages.ERROR, 'Sorry ...')
        #     return HttpResponseRedirect('#contact')

    return render(request, 'intro/index.html', {'form': form_class, })


def privacy_policy(request):

    return render(request, 'intro/privacy_policy.html')
