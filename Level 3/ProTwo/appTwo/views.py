from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from . import forms

# Create your views here.
# def index(request):
#     return HttpResponse("<em>My Second Project</em>")

def help(request):
    helpdict = {'help_insert':'HELP PAGE'}
    return render(request,'appTwo/help.html',context=helpdict)

def index(request):
    return render(request,'appTwo/index.html')

# def users(request):
#     user_list = User.objects.order_by('first_name')
#     user_dict = {"users":user_list}
#     return render(request,'appTwo/users.html',context=user_dict)

def users(request):
    form=forms.MyUsers()

    if request.method=='POST':
        form=forms.MyUsers(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR FORM INVALID")
            
    return render(request,'appTwo/users.html',{'forms':form})