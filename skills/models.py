from django.db import models
from django.conf import settings
from django.db.models import Avg
from django.utils.text import slugify
from django.contrib.auth import get_user_model

User = get_user_model()

CATEGORIES =  [
        ('TC', 'Technical'),
        ('CR', 'Crafts'),
        ('LN', 'Languages'),
        ('HI', 'Home Improvement'),
        ('HB', 'Health & Beauty'),
        ('OT', 'Other')
]

class AddSkills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userOffer')
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=2, choices=CATEGORIES, default='OT')
    availability = models.BooleanField()
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=200) # very big, please make it look better
    average_rating = models.FloatField(default=0.0)
    slug = models.SlugField(blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:                         # first time only
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class RequestSkills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userReq')
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=2, choices=CATEGORIES, default='OT')
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    

    def __str__(self):
        return self.category


