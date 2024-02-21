from django.views.generic import CreateView, ListView
from django.shortcuts import render
from django.contrib import messages
from .models import Reservation
from .forms import BookingForm


class BookingFormView(CreateView):
    """
    View to render booking form
    for user to make a reservation
    """
    template_name = 'booking/booking.html'
    form_class = BookingForm
    success_url = "/booking/reservations/"
    
    def form_valid(self, form):

        reservation = form.save(commit=False)
        reservation.guest = self.request.user

        # Check for availability
        reservation_date = form.cleaned_data['reservation_date']
        reservation_time = form.cleaned_data['reservation_time']

        # Count how many existing reservations there is on requested date and time
        existing_table_reservation = Reservation.objects.filter(
            reservation_date=reservation_date,
            reservation_time=reservation_time).count()

        # Checks that there is not 10 existing reservations on the requested date and time
        if existing_table_reservation == 10:
            message = f"Tables are fully booked for {reservation_date} at {reservation_time}, Please try another date and time"
            messages.error(self.request, message)
            return super().form_invalid(form)

        else:
            reservation.save()
            message = f"Your reservation for {reservation_date} at {reservation_time} is confirmed!"
            messages.success(self.request, message)
            return super().form_valid(form)
            


class ReservationsViews(ListView):
    template_name = 'booking/reservations.html'
    model = Reservation

    def get_queryset(self):
        return Reservation.objects.filter(guest=self.request.user)
