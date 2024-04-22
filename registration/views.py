from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader #for routing your templates
from django.views.decorators.csrf import csrf_exempt
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


@csrf_exempt
def addstudent(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")


        mydata = {"username": username, "email": email, "password":password}
        print(mydata)

        query = student(username=username, email=email,password= password)
        query.save()

        #fetch the student data to be displayed
        data = student.objects.all()
        context = {"data": data}
        return render(request,"register.html", context)

def editstudent(request,id):
    data = student.objects.get(id=id);
    context = {"data": data}
    return render(request,"updatestudent")

def updatestudent(request,id):
    if request.meethod == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        #modify the student details based on the student id given
        editstudent = student.objects.get(id=id)
        editstudent.username = username
        editstudent.email = email
        editstudent.password = password
        editstudent.save()
        return redirect("/dashboard")

def deletestudent(request,id):
    deletestudent = student.objects.get(id=id)
    deletestudent.delete()
    return redirect("/dashboard")