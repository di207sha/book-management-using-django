from django.contrib import admin
from django.urls import path
from .views import hello,signup,viewbook,login,addbook,add1

urlpatterns = [
    path("",hello),
    path("signup/",signup),
    path("viewbook/",viewbook),
    path("login/",login),
    path("add-book/",addbook),
    path("add-book/add",add1)
]