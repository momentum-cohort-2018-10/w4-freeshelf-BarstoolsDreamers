from django.forms import ModelForm
from collection.models import Book, BookCategory, MapBookCategory


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'description',)


# class BookCategoryForm(forms.ModelForm):
#     class Meta:
#         model = BookCategory
