from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def table_booking(request):
    return HttpResponse("Here can you book a table")