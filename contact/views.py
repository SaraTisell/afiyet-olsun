from django.shortcuts import render
from .forms import ContactUsForm


def contact_us(request):

    if request.method == "POST":
        contactus_form = ContactUsForm(data=request.POST)
        if contactus_form.is_valid():
            contactus_form.save()


    contactus_form = ContactUsForm()

    return render(
        request, 
        "contact/contact.html",
        {"contactus_form": contactus_form

        },
    )
