from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from crud.models import employees

# Create your views here.


def signup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password1 = request.POST.get("password1")

        if password != password1:
            return HttpResponse("Password doesnot match")
        else:
            user=User.objects.create_user(username=name, password=password)

        return redirect("/")


    return render(request, "signup.html")


def signin(request):
    if request.method== "POST":
        username=request.POST.get("username")
        password11= request.POST.get("password11")

        user= authenticate(request, username=username, password= password11)
        if user is not None:
            login(request, user)
            return redirect("/home/")

    return render(request, "signin.html")

@login_required(login_url="signin")
def home(request):
    detail=employees.objects.all()
    return render(request, "home.html",{
        "detail":detail
    })

def logout_view(request):
    logout(request)
    return redirect("/")