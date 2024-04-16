from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader #for routing your templates
from .models import student
def registration(request):
    return HttpResponse("Welcome to registration!")

def mypage(request):
    template = loader.get_template("register.html")
    return HttpResponse(template.render())

def register(request):
    template = loader.get_template("register.html")
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template("login.html")
    return HttpResponse(template.render())

def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())

def dashboard(request):
    template = loader.get_template("dashboard.html")
    return HttpResponse(template.render())

def addstudent(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        mydata = {"username": username, "email": email, "password":password}
        print(mydata)

        query = student(username, email, password)
        query.save()

