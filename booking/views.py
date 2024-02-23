from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Reservation
from .forms import BookingForm


class BookingFormView(LoginRequiredMixin, CreateView):
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


class ViewReservations(LoginRequiredMixin, ListView):
    """
    View to display existing reservations
    Own reservations for user
    All reservations for staff
    """
    model = Reservation 
    template_name = 'booking/reservations.html'

    def get_queryset(self):

        if self.request.user.is_staff:
            return Reservation.objects.all()
        else:
            return Reservation.objects.filter(guest=self.request.user)

  


class UpdateReservation(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    """
    Function to update an existing reservation
    Using the same logic as in the BookingformView
    but excludes the current reservation that is getting updated.
    """
    model = Reservation
    form_class = BookingForm
    template_name = 'booking/update_reservation.html'
    success_url = reverse_lazy('reservations')
    success_message = "Your reservation was successfully Updated!"

    def form_valid(self, form):

        reservation = form.save(commit=False)

        # Check for availability
        reservation_date = form.cleaned_data['reservation_date']
        reservation_time = form.cleaned_data['reservation_time']

        # Count how many existing reservations there is on requested date and time
        # Excluding the reservations that is under editing
        existing_table_reservation = Reservation.objects.filter(
            reservation_date=reservation_date,
            reservation_time=reservation_time).exclude(reservation_id=reservation.reservation_id).count()

        # Checks that there is not 10 existing reservations on the requested date and time
        if existing_table_reservation == 10:
            message = f"Sorry the requested {reservation_date} and {reservation_time} is not available. Please try another date and time"
            messages.error(self.request, message)
            return super().form_invalid(form)

        else:
            reservation.save()
            return super().form_valid(form)

    def test_func(self):
        """ Test user is staff """
        if self.request.user.is_staff:
            return True
        else:
            return self.request.user == self.get_object().guest    



class DeleteReservation(UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    """
    Function to delete an existing reservation
    """
    model = Reservation
    template_name = 'booking/delete_reservation_confirm.html'
    success_url = reverse_lazy('reservations')
    success_message = "Your reservation was successfully Canceled!"

    def test_func(self):
        """ Test user is staff """
        if self.request.user.is_staff:
            return True
        else:
            return self.request.user == self.get_object().guest
