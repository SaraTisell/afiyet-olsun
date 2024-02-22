from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from .models import ContactRequest
from .forms import ContactUsForm


class ContactUsView(CreateView):
    """
    View to contact form for user to send a request
    Account is not mandatory to send a contact request
    After submission is the user sent to a "Thank You" page
    """
    model = ContactRequest
    form_class = ContactUsForm
    template_name = 'contact/contact.html'
    success_url = reverse_lazy('contact_success')


class ContactSuccessView(TemplateView):
    """
    Renders "Thank you" page after contact form submission
    """
    template_name = 'contact/contact_success.html'