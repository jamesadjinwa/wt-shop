from django.db import models
from django import forms
from django.core.validators import RegexValidator


phoneValidator = RegexValidator(r'^(\+237\d{9}|\d{9})$',
                                'Sorry! Valid format: +237 followed by 9 digits allowed.')

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
    contact_phone = forms.CharField(required=True, validators=[phoneValidator], max_length=13, widget=forms.TextInput(
        # contact_phone = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'type': 'tel',
            'class': 'form-control',
            'placeholder': "Your Phone *",
            'id': 'phone',
            'pattern': '^(\+237\d{9}|\d{9})$'
        }
    ))
    contact_message = forms.CharField(required=True, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': "Your Message *",
            'id': 'message'
        }
    ))
