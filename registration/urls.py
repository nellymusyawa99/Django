from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path("registerpage/", views.mypage, name='myregisterpage')#views.mypage calls the function in views.py line 7

]