from django.shortcuts import render, redirect
from . import forms
from .models import AddSkills
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "index.html")

def skillboard(request):
    skills = AddSkills.objects.all()
    return render(request, 'skills/skillboard.html', {'skills': skills})

@login_required
def addSkills(request):
    if request.method == 'POST':
        form = forms.AddSkillsForm(request.POST, request.FILES)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.username = request.username
            skill.save()
            return redirect('skillboard')

    else:
        form = forms.AddSkillsForm()
    return render(request, 'skills/addskills.html', {'form': form})