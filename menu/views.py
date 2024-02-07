from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view_menu(response):
    return HttpResponse("Here is our menu")