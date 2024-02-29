from django.urls import path
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path(
        'menu/',
        TemplateView.as_view(template_name='home/menu.html'), name='menu')
]
