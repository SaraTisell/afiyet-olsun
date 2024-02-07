from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def user_review(request):
    return HttpResponse("Reviews from guests will be displayed here")
