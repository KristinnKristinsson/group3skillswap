from django import forms
from django.contrib.auth.models import User


class SkillsForm(forms.ModelForm): #allows us to create forms directly from Modelform

    #password = forms.CharField(widget=forms.PasswordInput) #overrides the pwd default behavior - 
                                                           #pwdInput will hide pwd input under dots in the HTML form!

    class Meta():  #tells django to base the model on User
        model = User
        fields = ('username','email','password') #the original user fields of native User


class SkillsForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo #build on UserProfileInfo which added portfoliosite and userpic
        fields = ('Skill Title','Category','Description', 'Availability', 'Location')

class theSkill(forms.Form):
    title = forms.CharField()
    category = forms.EmailField()
    description = forms.CharField(widget=forms.Textarea)
    availability = forms.CharField(widget=forms.Textarea)
    location = forms.CharField(widget=forms.Textarea)