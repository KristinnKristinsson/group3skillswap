from django.shortcuts import render
from user_authentication.forms import Form, UserProfileForm
from user_authentication.models import UserProfile

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,'skills/index.html')

@login_required 
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method== 'POST':
        user_form = Form(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user =user

            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)

    else: 
        user_form = Form()
        profile_form = UserProfileForm()
    
    return render(request, 'skills/registration.html',
                  {'user_form':user_form,
                   'profile_form':profile_form,
                   'registered':registered})
            
             
def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account Not active')
        else:
            print("Someone tried to login but failed!")
            print('username: {} and password {}'.format(username,password))
            return HttpResponse("Invalid login details supplied!")
    else:
        return render(request,'skills/login.html')