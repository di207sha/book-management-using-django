from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return render(request,"firstpage.html")
def signup(request):
    return render(request,"signup.html")
def viewbook(request):
    return render(request,"viewbook.html")
def login(request):
    return render(request,"login.html")