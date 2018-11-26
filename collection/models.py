import datetime
from django.db import models
from django.utils import timezone


class BookCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.CharField(max_length=1024)
    slug = models.SlugField(unique=True)
    date_added = models.DateTimeField('date added')
    image_file = models.CharField(max_length=200)
    url = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title + " (" + self.author+")"

    class Meta:
        unique_together = ('title', 'author',)


class MapBookCategory(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.category.name + " | " + self.book.title

    class Meta:
        unique_together = ('book', 'category')
