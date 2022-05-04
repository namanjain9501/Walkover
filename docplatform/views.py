from django.shortcuts import render,redirect
from . forms import *
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def home(request):
    return render(request,'workspace.html')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ("Admin Registered Successfully"))
            return redirect('login')
            
        else:
            messages.success(request, ("Form is invalid!"))
            return redirect('register')
    else: 
        form = SignUpForm()        
        return render(request,'register.html',{'form':form})


def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            try:
                user = authenticate(username=User.objects.get(email=username), password=password)
            except:
                user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('register')
            else:
                messages.success(request, ("Invalid Credentials!"))
                return redirect('login')
        else:
            messages.success(request, ("There was an ERROR Loggin in. Try again"))
            return redirect('login')
    return render(request,'login.html',{'form':form,})