from django.contrib import admin
from django.urls import path
from .views import hello,signup

urlpatterns = [
    path("",hello),
    path("signup/",signup),
    path("view")
]