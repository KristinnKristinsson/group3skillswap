from django.urls import path
from .views import browse, skill_view, reverse_skill_view

app_name = 'browse'

urlpatterns = [
    path('browse/', browse, name='browse'),
    path('user/<str:username>/', skill_view, name='skills_by_user'),
    path('user/<str:username>/<str:skill_name>/', skill_view, name='skill_detail_from_user'),
    path('skill/<str:skill_name>/', reverse_skill_view, name='users_by_skill'),
    path('skill/<str:skill_name>/<str:username>/', reverse_skill_view, name='skill_detail_from_skill'),
]