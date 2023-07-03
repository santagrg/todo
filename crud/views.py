from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import employees
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout



# Create your views here.
@login_required(login_url="signin")
def employee(request):
    if request.method=="POST":
        e_name=request.POST.get("e_name")
        e_address=request.POST.get("e_address")
        e_phone=request.POST.get("e_phone")
        e_email=request.POST.get("e_email")

        emp = employees()
        emp.ename = e_name
        emp.eaddress = e_address
        emp.ephone = e_phone
        emp.eemail = e_email

        emp.save()

        return redirect("/home/")


    return render(request, "addemp.html")

def edelete(request, roll):
    em = employees.objects.get(pk=roll)
    em.delete()
    return redirect("/home/")

@login_required(login_url="signin")
def edit_emp(request, roll):
    emp = employees.objects.get(pk=roll)
    return render(request, "edit.html", {
        "emp":emp
    })

def do_edit_emp(request, roll):
    if request.method=="POST":
        nname=request.POST.get("nname")
        nemail=request.POST.get("nemail")
        nphone=request.POST.get("nphone")
        naddress=request.POST.get("naddress")

        n = employees.objects.get(pk=roll)
        n.ename=nname
        n.eemail=nemail
        n.ephone=nphone
        n.eaddress=naddress

        n.save()

        return redirect("/home/")

