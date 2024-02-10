"""
URL configuration for afiyet_olsun project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from home import views as index_views
#from contact import views as contact_views
#from reviews import views as reviews_views
#from menu import views as menu_views
#from booking import views as booking_views

urlpatterns = [
#   path('', index_views.index, name='index'),
    path('', include('home.urls'), name="home-urls"),
    path('admin/', admin.site.urls),
    path('reviews/', include("reviews.urls"), name="reviews-urls"),
#    path('booking/', include('booking.urls')),
#    path('contact/', contact_views.contact_us, name='contact'),
#    path('menu/', menu_views.view_menu, name='menu'),
#    path('reviews/', reviews_views.user_review, name='reviews'),
    
    
]
