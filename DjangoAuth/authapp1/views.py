from django.shortcuts import render
from django.views.generic.list import ListView
#don't use default form  -> from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterNew
from django.contrib import messages
from .models import UserData

def index(request):
    return render(request, 'authapp1/index.html')


def register(request):
    form = UserRegisterNew()
    if request.method == "POST":
        form = UserRegisterNew(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ("User created successfuly"))

    return render(request, 'authapp1/register.html', {'form': form})


def detail(request, slug):
    datas = UserData.objects.filter(username=slug)
    return render(request, 'authapp1/detail.html', {'datas': datas})