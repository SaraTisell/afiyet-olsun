from django.urls import path
from .views import (
    ContactUsView,
    ContactSuccessView,
    ContactInboxView,
    ContactDetailsView,
    ContactInboxStaff
)


urlpatterns = [
    path('', ContactUsView.as_view(), name='contact'),
    path(
        'contact_success/',
        ContactSuccessView.as_view(), name='contact_success'),
    path('inbox/', ContactInboxView.as_view(), name='inbox'),
    path('inbox/<int:pk>/', ContactDetailsView.as_view(), name='inbox_details')
]
