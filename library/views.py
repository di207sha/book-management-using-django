from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
# Create your views here.
def hello(request):
    return render(request,"firstpage.html")
def signup(request):
    return render(request,"signup.html")
def viewbook(request):
    return render(request,"viewbook.html")
def login(request):
    return render(request,"login.html")
def addbook(request):
    if request.method=="POST":
        i=request.POST["isbn no"]
        t=request.POST["title"]
        a=request.POST["author"]
        y=request.POST["year"]
        book=Book()
        book.isbn_no=i
        book.book_name=t
        book.author_name=a
        book.published_year=y
        book.save()
        return HttpResponse("/add-book")
    return render(request,"addbook.html")