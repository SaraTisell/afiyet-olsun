from django.urls import path
from . import views


urlpatterns = [
    path('', views.BookingFormView.as_view(), name='booking'),
    path('reservations/', views.ReservationsViews.as_view(), name='reservations')
]