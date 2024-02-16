from django.shortcuts import render
from .models import Reservation
from .forms import BookingForm


# Create your views here.
def booking(request):
    form = BookingForm()
    return render(request, 'booking/booking.html', {'booking_form': form})