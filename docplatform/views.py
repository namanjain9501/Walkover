from django.shortcuts import render,redirect
from . forms import *
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import FileResponse, Http404, HttpResponse
import os

# def content(request,id):
#     docx = Doc.objects.get(pk=id) 
#     with open('/path/to/my/file.pdf', 'r') as pdf:
#         response = HttpResponse(pdf.read(), mimetype='application/pdf')
#         response['Content-Disposition'] = 'inline;filename=some_file.pdf'
#         return response
#     pdf.closed

def front(request):
    workspace_list = Workspace.objects.all()
    return render(request,'front.html', {'workspace_list':workspace_list})

def create(request):
    if request.method == 'POST':
        form = Createform(request.POST)
        if form.is_valid():
            worksp = form.save(commit=False)
            worksp.admin = request.user
            worksp.save() 
            return redirect('content')
    form = Createform()
    return render(request, 'create.html', {'form': form})

    
def content(request,id):
    docx = Doc.objects.get(pk=id) 
    module_dir = os.path.dirname(__file__)  
    file = str(docx.doc)
    file_path = os.path.join(module_dir, file) 
    data_file = open(file_path , 'rb')       
    with open(file_path, 'rb') as pdf:
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = 'filename=some_file.pdf'
        return response
        

    



def upload(request):
    if request.method == 'POST':
        form = Uploadform(request.POST, request.FILES)
        if form.is_valid():
            docx = form.save(commit=False)
            docx.uploaded_by = request.user
            docx.save() 
            return redirect('register')
    form = Uploadform()
    return render(request, 'upload.html', {'form': form})

def list(request):
    doc_list = Doc.objects.all()
    return render(request,'workspace.html',{'list':doc_list})
    

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ("User Registered Successfully"))
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