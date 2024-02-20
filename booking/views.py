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
    success_url = '#'
    
    def form_valid(self, form):

        reservation = form.save(commit=False)
        reservation.guest = self.request.user

        # Check for availability
        reservation_date = form.cleaned_data['reservation_date']
        reservation_time = form.cleaned_data['reservation_time']
        company_size = form.cleaned_data['company_size']

        # Check if tables is available for requested company size on desired date and time
        #available_tables = Table.objects.filter(availability=True, capacity__in=[company_size + 1])
"""
        for table in available_tables:     
            existing_table_reservation = Reservation.objects.filter(
                reservation_date=reservation_date,
                reservation_time=reservation_time,

            )
            if not existing_table_reservation.exists():
                reservation.table_id = table
                reservation.save()
                return super().form_valid(form)
"""
        







"""
    def form_valid(self, form):
        form.save()

    


    def booking_view(request):
        form = BookingForm()
        return render(request, 'booking/booking.html', {'booking_form': form})
"""

class ReservationsViews(ListView):
    template_name = 'booking/reservations.html'
    model = Reservation

    def get_queryset(self):
        return Reservation.objects.filter(guest=self.request.user)