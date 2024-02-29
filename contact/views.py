from django.views.generic import CreateView, TemplateView, ListView, DetailView
from django.contrib.auth.mixins import UserPassesTestMixin
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


class ContactInboxStaff(TemplateView):

    template_name = 'contact/inbox.html'


class ContactInboxView(UserPassesTestMixin, ListView):
    """
    View for staff to see contact requests
    """

    model = ContactRequest
    template_name = 'contact/inbox.html'
    get_success_url = reverse_lazy('inbox')

    def get_queryset(self):

        if self.request.user.is_staff:
            return ContactRequest.objects.all()

    def test_func(self):
        """ Test user is staff """
        if self.request.user.is_staff:
            return True


class ContactDetailsView(UserPassesTestMixin, DetailView):
    """
    View for staff to se details of the contact requests
    """

    model = ContactRequest
    template_name = 'contact/inbox_details.html'

    def test_func(self):
        """ Test user is staff """
        if self.request.user.is_staff:
            return True
