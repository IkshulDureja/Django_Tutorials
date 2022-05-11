from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm

# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")

def register(request):
    
    registered=False;

    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            #save info directly into database
            user=user_form.save()

            #hashing the password through Settings.py
            user.set_password(user.password)

            #update using hashed password
            user.save()

            profile = profile_form.save(commit=False)

            profile.user=user

            if 'profile_pic' in request.FILES:
                print('Found it')
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered=True

        else:
            print(user_form.errors,profile_form.errors)
    
    else:
        #not POST request
        user_form=UserForm()
        profile_form=UserProfileInfoForm()
    
    return render(request,'basic_app/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})


def user_login(request):

    if request.method=='POST':

        username= request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE!")
        else:
            print("Someone tried to login and failed!")

            print("Username:{} and Password:{}".format(username,password))

            HttpResponse("Invalid login details supplied!")
    else:
        #not a post request
        return render(request,'basic_app/login.html',{})

