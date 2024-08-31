from django.contrib import admin
from django.urls import path
from .views import hello,signup,viewbook,login

urlpatterns = [
    path("",hello),
    path("signup/",signup),
    path("viewbook/",viewbook),
    path("login/",login)
]