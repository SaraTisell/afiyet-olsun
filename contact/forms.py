from django import forms
from .models import Message
from datetime import datetime


class ContactUsForm(forms.ModelForm):

    class Meta:
        model = Message
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