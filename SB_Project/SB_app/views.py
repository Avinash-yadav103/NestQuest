from django.shortcuts import render
from django.contrib.auth.models import User



def HomeView(request):
    return render(request, "index.html")

def FormView(request):
    return render(request, "forms/form.html")

def LoginView(request):
    return render(request, "forms/login.html")
