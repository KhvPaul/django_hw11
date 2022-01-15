from django.contrib import admin

from .models import Author, Book, Publisher, Store

# Register your models here.


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'age']


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'pages', 'price', 'rating', 'publisher', 'pubdate']


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name']
