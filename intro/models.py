from django.db import models

from django.core.validators import RegexValidator

# Create your models here.

phoneValidator = RegexValidator(r'^(\+237[62][2356789]\d{7}|[62][2356789]\d{7})$',
                                'Enter a valid Cameroon phone number.')


class Contact(models.Model):

    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_phone = models.CharField(validators=[phoneValidator], max_length=13)
    contact_message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
