from django import forms
from .models import ContactRequest
from datetime import datetime


class ContactUsForm(forms.ModelForm):

    class Meta:
        model = ContactRequest
        fields = [
            'name',
            'email',
            'title',
            'message'
        ]

        labels = {
            'name': 'Name',
            'email': 'Email address',
            'title': 'Subject',
            'message': 'Message'
        }