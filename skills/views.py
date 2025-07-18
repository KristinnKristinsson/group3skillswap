from django.shortcuts import render, redirect
#from django.http import HttpResponse
from .models import AddSkills
from .forms import AddSkillsForm, RequestSkillsForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    #return HttpResponse("<h1>It works</h1>")
   return render(request, 'index.html')

# def skillboard(request):
#     skills = AddSkills.objects.all()
#     return render(request, 'skills/skillboard.html', {'skills': skills})
# RequestSkills.objects.all()  #has to be DB object from models

def skillboard(request):
    addskills = AddSkillsForm() 
    getskills = RequestSkillsForm()
    return render(request, 'skills/skillboard.html', {'addskills': addskills, 'getskills':getskills})

@login_required
def addSkills(request):
    if request.method == 'POST':
        added=AddSkillsForm(request.POST) #creates instance of ModelForm
        if added.is_valid():
            fromDB=added.save(commit=False) #create filled in instance of Model, do not commit
            fromDB.user=request.user  #add user to the form - is the connections CORRECT?? XX
            fromDB.save()             #commit to DB
            messages.
            return redirect('skills:skillboard')
        else:
            return redirect('skills:skillboard')
    else: #GET
        return redirect('skills:skillboard')
      
@login_required
def reqSkills(request):
    if request.method == 'POST':
        req=RequestSkillsForm(request.POST) #creates instance of ModelForm
        if req.is_valid():
            fromDB=req.save(commit=False) #create filled in instance of Model, 
                                   #do not commit-don't forget to save the instance
            fromDB.user=request.user  #add user to the form
            fromDB.save()             #commit to DB
            return redirect('skills:skillboard')
        else:
            return redirect('skills:skillboard')
    else: #GET
        return redirect('skills:skillboard')
        
