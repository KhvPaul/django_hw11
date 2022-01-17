from django.contrib import admin
from django.core.management import BaseCommand
from django.db.models import Avg

from .models import Author, Book, Publisher, Store

# Register your models here.

admin.site.site_header = 'HW11 Dashboard'


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'books_count']
    search_fields = ['name']
    list_filter = ['age']
    fields = ['name', 'age', 'show_books']
    sortable_by = ['age', 'books_count']

    def books_count(self, obj):
        books = Book.objects.filter(authors=obj)
        return books.count()

    books_count.short_description = 'Books Count'

    def show_books(self, obj):
        books, out = Book.objects.filter(authors=obj), ''
        for book in books:
            out += book.name + '\n'
        return out

    show_books.short_description = 'Books'


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name', 'books_count']
    search_fields = ['name']
    fields = ['name']

    def books_count(self, obj):
        books = Book.objects.filter(publisher=obj)
        return books.count()

    books_count.short_description = 'Books Count'


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'pages', 'price', 'publisher', 'pubdate', 'books_count']
    search_fields = ['name', 'publisher']
    list_filter = ['pubdate']
    readonly_fields = ['name', 'pages', 'publisher', 'pubdate', 'show_authors']
    fields = ['name', 'pages', 'rating', 'price', 'publisher', 'pubdate', 'show_authors']
    sortable_by = ['pages', 'rating', 'price', 'pubdate']

    def books_count(self, obj):
        count = obj.authors.count()
        return count

    books_count.short_description = 'Authors count'

    def show_authors(self, obj):
        authors, out = obj.authors.all(), ''
        for author in authors:
            out += author.name + '\n'
        return out

    show_authors.short_description = 'Authors'


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'books_count', 'avg_price']
    search_fields = ['name']

    def books_count(self, obj):
        count = obj.books.count()
        return count

    books_count.short_description = 'Books Count'

    def avg_price(self, obj):
        avg = obj.books.aggregate(Avg("price"))
        return round(avg['price__avg'], 5)

    avg_price.short_description = 'Avg Book Price'
