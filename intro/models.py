from django.db import models
from django import forms


# Create your models here.


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    phone_regex = forms.RegexField(regex=r'^\+237\d{9}$',
                                   error_message='Phone number must be entered in the format: \'+237\'. Up to 12 digits allowed.'
                                   )
    contact_phone = forms.CharField(required=True, validators=[phone_regex])
    contact_message = forms.CharField(required=True, widget=forms.Textarea)
