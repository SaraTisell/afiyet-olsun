from django.urls import path
from .views import BookingFormView, ViewReservations, UpdateReservation, DeleteReservation


urlpatterns = [
    path('', BookingFormView.as_view(), name='booking'),
    path('reservations/', ViewReservations.as_view(), name='reservations'),
    path('reservation/<str:pk>/update', UpdateReservation.as_view(), name='reservation_update'),
    path('reservation/<str:pk>/delete', DeleteReservation.as_view(), name= 'reservation_delete'),

]