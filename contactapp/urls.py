from django.urls import path
from . import views

app_name = 'contactapp'

urlpatterns = [
    path('contact_index/', views.contact_index, name='contact_index'),
    path('thankyou_page/', views.thankyou_page, name='thankyou_page'),
 
]