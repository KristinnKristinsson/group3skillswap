from django.db import models
from django.contrib.auth.models import User 

CATEGORIES =  [
        ('TC', 'Technical'),
        ('CR', 'Crafts'),
        ('LN', 'Languages'),
        ('OT', 'Other')
]

class AddSkills(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    date = models.DateField()
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=2, choices=CATEGORIES, default='OT')
    description = models.TextField()
    availability = models.TextField()
    location = models.TextField()
    profilePic = models.ImageField(default='fallback.png', blank=True)

    def __str__(self):
        return self.title


