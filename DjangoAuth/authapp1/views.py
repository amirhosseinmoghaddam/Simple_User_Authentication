from django.shortcuts import render
from django.views.generic.list import ListView
# i wasn't use default form  -> from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterNew
from django.contrib import messages
from .models import UserData

#first page func
def index(request):
    return render(request, 'authapp1/index.html')

#regiter page func
def register(request):
    #set register form
    form = UserRegisterNew()
    #save user info if valid
    if request.method == "POST":
        form = UserRegisterNew(request.POST)
        if form.is_valid():
            form.save()
            #register success message
            messages.success(request, ("User created successfuly"))
    #response
    return render(request, 'authapp1/register.html', {'form': form})

#user info func
def detail(request, slug):
    #Filter user info and render
    datas = UserData.objects.filter(username=slug)
    return render(request, 'authapp1/detail.html', {'datas': datas})
