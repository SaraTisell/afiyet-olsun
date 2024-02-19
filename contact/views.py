from django.shortcuts import render
from .forms import ContactUsForm


def contact_us(request):
    contactus_form = ContactUsForm()

    return render(
        request, 
        "contact/contact.html",
        {"contactus_form": contactus_form

        },
    )
