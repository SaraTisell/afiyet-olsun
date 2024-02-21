from django import forms
from .models import Reservation, RESERVATION_TIME, COMPANY_SIZE
from datetime import datetime


class BookingForm(forms.ModelForm):
    reservation_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'forms-input','type': 'date', 'min': datetime.now().date()}), label='Date')

    reservation_time = forms.ChoiceField(choices=RESERVATION_TIME, widget=forms.RadioSelect(), label='Time')

    company_size = forms.ChoiceField(choices=COMPANY_SIZE, widget=forms.Select, label='Number of Guests')

    class Meta:
        model = Reservation
        fields = [
            'guest_name',
            'email',
            'reservation_date',
            'reservation_time',
            'company_size',
            'additional_info'
        ]

        labels = {
            'guest_name': 'Name',
            'email': 'Email',
            'additional_info': 'Additional Information'
        }

        widgets = {
            'guest_name': forms.TextInput(attrs={'placeholder': 'Your Name','class': 'forms-input'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email Address', 'class': 'forms-input'}),
            'additional_info': forms.Textarea(attrs={'placeholder': 'If you have some special request or additional information, please write it here'}),
        }