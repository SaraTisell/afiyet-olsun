from django.urls import path
from .views import ContactUsView, ContactSuccessView


urlpatterns = [
    path('', ContactUsView.as_view(), name='contact'),
    path('contact_success/', ContactSuccessView.as_view(), name='contact_success')

]