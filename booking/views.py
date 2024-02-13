from django.shortcuts import render
from .models import Reservation


# Create your views here.
def booking(request):
    return render(request, 'booking/booking.html')