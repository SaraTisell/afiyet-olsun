from django.shortcuts import render
from django.views import generic
from .models import Review

# Create your views here.
class PostList(generic.ListView):
    queryset = Review.objects.all()
    template_name = "review_list.html"
