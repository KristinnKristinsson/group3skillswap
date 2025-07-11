from django.urls import path
from skills import views

app_name='skills'

urlpatterns = [
    path('skillboard/', views.skillboard, name='skillboard'),
    path('addSkills/', views.addSkills, name='addSkills'),
    
]
