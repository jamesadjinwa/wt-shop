from django.db import models
from django import forms


# Create your models here.


class ContactForm(forms.Form):

    contact_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'type': 'text',
            'class': 'form-control',
            'placeholder': "Your Name *",
            'id': 'name'
        }
    ))
    contact_email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={
            'type': 'email',
            'class': 'form-control',
            'placeholder': "Your Email *",
            'id': 'email'
        }
    ))
    phone_regex = forms.RegexField(regex=r'^\+237\d{9}$',
                                   error_message='Phone number must be entered in the format: +237 followed by 9 digits allowed.'
                                   )
    contact_phone = forms.CharField(required=True, validators=[phone_regex], widget=forms.TextInput(
        attrs={
            'type': 'tel',
            'class': 'form-control',
            'placeholder': "Your Phone *",
            'id': 'phone'
        }
    ))
    contact_message = forms.CharField(required=True, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': "Your Message *",
            'id': 'message'
        }
    ))
