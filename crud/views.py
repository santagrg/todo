from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import employees


# Create your views here.
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
    return redirect("/home")

def edit_emp(request):
    emp = employees.objects.get(pk=roll)
    return render(request, "edit,html", {
        "emp":emp
    })