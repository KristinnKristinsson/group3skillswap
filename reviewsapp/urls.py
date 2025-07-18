from django.urls import path
from . import views

app_name = "reviewsapp"

urlpatterns = [
    path('add-review/<str:username>/<int:skill_id>/<str:skill_name>/', views.add_review, name='add_review'),
    path('', views.review_list, name='review_list')

]
