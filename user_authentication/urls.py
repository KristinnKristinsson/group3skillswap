from django.urls import path
from user_authentication import views

app_name = 'user_authentication'

urlpatterns = [
    path('register/',    views.register,   name='register'),
    path('user_login/',  views.user_login, name='user_login'),
    path('user_logout/',  views.user_logout, name='user_logout'),
]
