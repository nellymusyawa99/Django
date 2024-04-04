from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader #for routing your templates
def registration(request):
    return HttpResponse("Welcome to registration!")

def mypage(request):
    template = loader.get_template("register.html")
    return HttpResponse(template.render())