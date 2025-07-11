from django import forms
from . import models

class AddSkillsForm(forms.ModelForm):
    class Meta:
        model = models.AddSkills
        fields = ['title','date', 'category','description','availability','location','profilePic']