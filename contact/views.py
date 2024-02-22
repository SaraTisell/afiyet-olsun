from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
#from django.shortcuts import render, redirect
#from django.contrib import messages
from .models import ContactRequest
from .forms import ContactUsForm


class ContactUsView(CreateView):
    model = ContactRequest
    form_class = ContactUsForm
    template_name = 'contact/contact.html'
    success_url = reverse_lazy('contact_success')


class ContactSuccessView(TemplateView):
    template_name = 'contact/contact_success.html'