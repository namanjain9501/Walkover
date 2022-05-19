import string
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

def test(request):
    return render(request,'test.html')


def front(request):
    workspace_list = Workspace.objects.all()
    workspace_joined = request.user.workspace
    return render(request,'front.html', {'workspace_list':workspace_list,'workspace_joined':workspace_joined})

def create(request):
    if request.method == 'POST':
        form = Createform(request.POST)
        if form.is_valid():
            worksp = form.save(commit=False)
            worksp.admin = request.user
            worksp.save() 
            return render(request, 'welcome.html', {'worksp': worksp})
    form = Createform()
    return render(request, 'create.html', {'form': form})




def join(request,id):
    worksp = Workspace.objects.get(pk=id) 
    request.user.workspace.add(worksp)
    return render(request, 'welcome.html', {'worksp': worksp})

def welcome(request,id):
    worksp = Workspace.objects.get(pk=id) 
    return render(request, 'welcome.html', {'worksp': worksp})



    
def content(request,id_doc,id_work):
    worksp = Workspace.objects.get(pk=id_work)
    doc_list = Doc.objects.filter(workspace=id_work)
    import os
    docx = Doc.objects.get(pk=id_doc) 
    module_dir = os.path.dirname("C:/Users/Naman/Desktop/Walkover/media/")  
    file = str(docx.doc)
    file_path = os.path.join(module_dir, file) 
    data_file = open(file_path , errors="ignore")       
    data = data_file.readlines()
    return render(request, 'show.html',{'doc': data,'list':doc_list,'workspace':worksp})

    # data_file = open(file_path , 'rb')       
    # with open(file_path, 'rb') as pdf:
    #     response = HttpResponse(pdf.read(),content_type='application/pdf')
    #     response['Content-Disposition'] = 'filename=some_file.pdf'
    #     return response

    
    import os

# def results(request):
#     module_dir = os.path.dirname(__file__)  
#     file_path = os.path.join(module_dir, 'data.txt')   #full path to text.
#     data_file = open(file_path , 'r')       
#     data = data_file.read()
#     context = {'rooms': data}
#     return render(request, 'javascript/results.html',context)
        

    




def list(request,id):
    worksp = Workspace.objects.get(pk=id)
    doc_list = Doc.objects.filter(workspace=id)
    return render(request,'list.html',{'list':doc_list, 'workspace':worksp})



def upload(request,id):
    worksp = Workspace.objects.get(pk=id)
    doc_list = Doc.objects.filter(workspace=id)
    if request.method == 'POST':
        form = Uploadform(request.POST, request.FILES)
        if form.is_valid():
            docx = form.save(commit=False)
            docx.uploaded_by = request.user
            docx.workspace = worksp
            docx.save()        
            return render(request,'list.html',{'list':doc_list, 'workspace':worksp})

    form = Uploadform()
    return render(request, 'upload.html', {'form': form})
    

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
                return redirect('front')
            else:
                messages.success(request, ("Invalid Credentials!"))
                return redirect('login')
        else:
            messages.success(request, ("There was an ERROR Loggin in. Try again"))
            return redirect('login')
    return render(request,'login.html',{'form':form,})

def logout_view(request):
    logout(request)
    messages.success(request, ("Logged Out"))
    return redirect('login')