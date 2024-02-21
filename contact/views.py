from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactUsForm


# Return Thank you page 
def form_success(request):
    return render(request, 'contact/contact_success.html')


def contact_us(request):
    """
    View to contact form for users to send a request
    Account is not mandatory to send a contact request
    After submission, user is sent to a 'Thank You page'
    """

    if request.method == "POST":
        contactus_form = ContactUsForm(data=request.POST)
        if contactus_form.is_valid():
            contactus_form.save()
            return redirect('contact_success')
            


    contactus_form = ContactUsForm()

    return render(
        request, 
        "contact/contact.html",
        {"contactus_form": contactus_form

        },
    )
