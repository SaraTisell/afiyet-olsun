from django.views.generic import CreateView, ListView
from django.shortcuts import render
from .models import Reservation, Table
from .forms import BookingForm


class BookingFormView(CreateView):
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
        available_tables = Table.objects.filter(availability=True, capacity__gte=company_size -1)





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