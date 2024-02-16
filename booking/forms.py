from django import forms
from .models import Reservation, RESERVATION_TIME
from datetime import datetime


class BookingForm(forms.ModelForm):
    reservation_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'max': datetime.now().date()}), label='Date')

    reservation_time = forms.ChoiceField(choices=RESERVATION_TIME, widget=forms.RadioSelect(), label='Time')

    class Meta:
        model = Reservation
        fields = [
            'guest_name',
            'reservation_date',
            'reservation_time',
            'company_size',
            'additional_info'
        ]

        labels = {
            'guest_name': 'Name',
            'company_size': 'Number of Guests',
            'additional_info': 'Additional Information'
        }
