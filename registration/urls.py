from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path("registerpage/", views.mypage, name='myregisterpage'),#views.mypage calls the function in views.py line 7
    path("", views.home, name='home'),
    path("login/", views.login, name='login'),
    path("dashboard/", views.dashboard, name='dashboard'),
    path("addstudent", views.addstudent, name='addingstudent'),
    path("editstudent/<id>", views.editstudent, name='editstudent'),
    path("updatestudent/<id>", views.updatestudent, name='updatestudent'),
    path("deletestudent/<id>", views.deletestudent),



]