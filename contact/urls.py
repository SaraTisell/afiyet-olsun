from django.urls import path
from . import views


urlpatterns = [
    path('', views.contact_us, name='contact'),
    path('contact_success/', views.form_success, name='contact_success')

]