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
    return render(request,"addbook.html")
def add1(request):
    if request.method == 'POST':
        isbn_no = request.POST.get('isbn_no')
        book_name = request.POST.get('title')
        author_name = request.POST.get('author')
        published_year = request.POST.get('year')

        # Check if all fields are provided
        if isbn_no and book_name and author_name and published_year:
            try:
                # Convert isbn_no and published_year to integers
                isbn_no = int(isbn_no)
                published_year = int(published_year)
                
                # Create and save a new book entry
                Book.objects.create(
                    isbn_no=isbn_no,
                    book_name=book_name,
                    author_name=author_name,
                    published_year=published_year
                )
                return HttpResponse('Book added successfully!')
            except ValueError:
                return HttpResponse('Invalid data format. Please check your input.')
            except Exception as e:
                return HttpResponse(f'Error occurred: {e}')
        else:
            return HttpResponse('All fields are required!')
    return render(request, 'addbook.html')