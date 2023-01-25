from django.shortcuts import render,HttpResponseRedirect
from pra.forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def sign_up(request):
    if request.method=="POST":
        dj=SignUpForm(request.POST)
        if dj.is_valid():
            messages.success(request,"you Successfully Registered")
            dj.save()
            
    else:
        dj=SignUpForm()
    return render(request, 'pra/signup.html',{'form':dj})

 # login 
def user_login(request):
    if not request.user.is_authenticated:
        if request.method== "POST":
            dj=AuthenticationForm(request=request, data=request.POST)
            if dj.is_valid():
                uname=dj.cleaned_data['username']
                upass=dj.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,"You logged in Successfully!")
                    return HttpResponseRedirect('/profile/')
        else:
            dj=AuthenticationForm()
        return render(request, 'pra/login.html',{'form':dj})
    else:
        return HttpResponseRedirect('/profile/')
def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'pra/profile.html', {"name":request.user})
    else:
        return HttpResponseRedirect('/login/')
        
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')