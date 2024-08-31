from django.contrib import admin
from django.urls import path
from .views import hello,signup,viewbook,login,addbook

urlpatterns = [
    path("",hello),
    path("signup/",signup),
    path("viewbook/",viewbook),
    path("login/",login),
    path("add-book/",addbook)
]