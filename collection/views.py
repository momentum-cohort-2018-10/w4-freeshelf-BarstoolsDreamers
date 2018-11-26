from django.shortcuts import render, redirect
from collection.forms import BookForm
from collection.models import Book, BookCategory, MapBookCategory


def index(request):
    bookList = Book.objects.order_by('-title')
    book_category_list = BookCategory.objects.order_by('-name')
    context = {'bookList': bookList, 'categoryList': book_category_list}
    return render(request, 'collection/templates/index.html', context)


def book_detail(request, slug):
    book = Book.objects.get(slug=slug)
    return render(request, 'books/book_detail.html', {
        'book': book,
    })


def edit_book(request, slug):
    book = Book.objects.get(slug=slug)
    form_class = BookForm
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=book)
        if form.isvalid():
            form.save()
            return redirect('book_detail', slug=book.slug)

    else:
        form = form_class(instance=book)

    return render(request, 'books/edit_book.html', {
        'book': book,
        'form': form,
    })
