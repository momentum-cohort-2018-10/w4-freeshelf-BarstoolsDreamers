from django.core.management.base import BaseCommand
from django.conf import settings
import os.path
import csv
from collection.models import Book
from django.core.files import File


def get_path(file):
    return os.path.join(settings.BASE_DIR, 'initial_data', file)


class Command(BaseCommand):
    help = "My shiny new management command."

    def add_arguments(self, parser):
        # parser.add_argument('sample', nargs='+')
        pass

    def handle(self, *args, **options):
        print("Deleting dogs...")
        Book.objects.all().delete()
        with open(get_path('books.csv'), 'r') as file:
            # os.path.join(settings.BASE_DIR, 'initial_data',
            #     'books.csv')) as file:
            reader = csv.DictReader(file)
            for row in reader:
                book = Book(
                    title=row['tile'],
                    author=row['author'],
                    description=row['description'],
                    slug=row['slug'],
                    date_added=row['date_added'],
                    python=row['python'],
                    css=row['css'],
                    javascript=row['javascript'],
                    ruby=row['ruby'],
                    virtual_lab=row['virtual_lab'],
                    c_sharp=row['c_sharp'],
                    matlab=row['matlab'],
                )
                book.picture.save(
                    row['image'],
                    File(open(get_path(row['image']), 'rb')))

                # (os.path.join(settings.BASE.DIR, 'initial_data',
                #                        row['image'])), 'rb'))
                book.save()
        print("Books loaded!")
