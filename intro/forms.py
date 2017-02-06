from django.forms import ModelForm
from django import forms
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget
from .models import Contact

# Create your forms here.


class ContactForm(ModelForm):

    captcha = ReCaptchaField(required=True, widget=ReCaptchaWidget())

    class Meta:

        model = Contact
        fields = ['contact_name', 'contact_email', 'contact_phone', 'contact_message', 'captcha']
        widgets = {
            'contact_name': forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': "Your Name *",
                'id': 'name'
            }),
            'contact_email': forms.TextInput(attrs={
                'type': 'email',
                'class': 'form-control',
                'placeholder': "Your Email *",
                'id': 'email'
            }),
            'contact_phone': forms.TextInput(attrs={
                'type': 'tel',
                'class': 'form-control',
                'placeholder': "Your Phone * eg: +237234567890",
                'id': 'phone',
                'pattern': '^(\+237[62][2356789]\d{7}|[62][2356789]\d{7})$'
            }),
            'contact_message': forms.Textarea(attrs={
                'class': 'form-control',
                'style': 'height:135px',
                'placeholder': "Your Message *",
                'id': 'message'
            }),
        }
