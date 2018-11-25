from django.shortcuts import render
from collection.models import Book

# Create your views here.


def index(request):
    books = Book.objects.all().order_by('date_added')
    return render(request, 'index.html', {
        'books': books,
    })
