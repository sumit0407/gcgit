from django.shortcuts import render
from .models import *
# Create your views here.

def Dashboard(request):
    return render(request,"app/admin_index.html")

def admin_signin(request):
    return render(request,"app/admin_signin.html")

def admin_signup(request):
    return render(request,"app/admin_signup.html")

def AdminSignUp(request):
    name=request.POST['name']
    email=request.POST['email']
    passw=request.POST['pass']
    repass=request.POST['repass']
    if name and email and passw and repass:
        if passw==repass:
            Admin.objects.create(Username=name,Email=email,Password=passw)
            return render(request,"app/admin_index.html")
        else:
            msg="Re-Enter Password Not Match"
            return render(request,"app/admin_signup.html",{'err':msg})
    else:
        msg="All Fields Are Reqqired"
        return render(request,"app/admin_signup.html",{'err':msg})

def AdminSigiIn(request):
    email=request.POST['email']
    passw=request.POST['pass']
    user=Admin.objects.filter(Email=email)
    if user[0].Email==email:
        if user[0].Password==passw:
            return render(request,"app/admin_index.html")
        else:
            msg="Password Is Wrong"
            return render(request,"app/admin_signin.html",{'err':msg})
   
    else:
        msg="Email Is Wrong"
        return render(request,"app/admin_signin.html",{'err':msg})

            
        


