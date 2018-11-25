from django.shortcuts import render
from collection.models import Book

# Create your views here.


def index(request):
    books = Book.objects.all().order_by('date_added')
    return render(request, 'index.html', {
        'books': books,
    })


def book_detail(request, slug):
    book = Book.objects.get(slug=slug)
    return render(request, 'books/book_detail.html', {
        'book': book,
    })
