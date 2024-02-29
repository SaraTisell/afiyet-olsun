from django import forms
from .models import ContactRequest
from datetime import datetime


class ContactUsForm(forms.ModelForm):
    """
    Contact form so user can send a contact request
    """

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
            'email': 'Email',
            'title': 'Subject',
            'message': 'Message'
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your Name', 'class': 'forms-input'}),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Your Email Address', 'class': 'forms-input'}),
            'title': forms.TextInput(attrs={
                'placeholder': 'Subject', 'class': 'forms-input'}),
            'message': forms.Textarea(attrs={
                'placeholder': 'Please write your message here'}),
        }
        