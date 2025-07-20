from django.urls import path
from skills.views import addSkills,reqSkills, skillboard, success

app_name='skills'

urlpatterns = [
    path('', skillboard, name='skillboard'),
    path('addSkills/', addSkills, name='addSkills'),
    path('reqSkills/', reqSkills, name='reqSkills'),
    path('success/', success, name='success')
    
]
