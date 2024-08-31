from django.db import models

class Book(models.Model):
    isbn_no=models.IntegerField()
    book_name=models.CharField(max_length=50)
    author_name=models.CharField(max_length=50)
    published_year=models.IntegerField()
     
    def __str__(self):
        return self.book_name
        

