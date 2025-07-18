from django import forms
from user_authentication.models import UserProfile
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Form(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('portfolio','profile_pic',)