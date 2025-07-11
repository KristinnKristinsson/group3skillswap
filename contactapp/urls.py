from django.urls import path
from . import views

urlpatterns = [
    path('contact_index', views.contact_index, name='contact_index'),
    path('thank-you_page', views.thankyou_page, name='thankyou'),
 
]