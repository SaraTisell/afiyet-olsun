from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def contact_us(request):
    return HttpResponse("This is the contact page")