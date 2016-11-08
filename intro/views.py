from django.shortcuts import render

# Create your views here.


def intro(request):

    return render(request, 'intro/index.html', {})


def contact(request):

    form_class = ContactForm

    return render(request, 'intro/index.html/#contact', {
        'form': form_class,
    })
