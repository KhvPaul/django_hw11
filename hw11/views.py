from abc import ABC

from django.db.models import Avg, Count, Func
from django.shortcuts import render
from django.views import generic

from .models import Author, Book, Publisher, Store


def index(request):
    num_authors = Author.objects.count()
    num_books = Book.objects.count()
    num_publishers = Publisher.objects.count()
    num_stores = Store.objects.count()
    return render(
        request,
        'index.html',
        context={'num_authors': num_authors, 'num_books': num_books,
                 'num_publishers': num_publishers, 'num_stores': num_stores},
    )


class AuthorListView(generic.ListView):
    queryset = Author.objects.all().prefetch_related('book_set').annotate(books_count=Count('book'))
    paginate_by = 25


class AuthorDetailView(generic.DetailView):

    class Round(Func, ABC):
        function = 'ROUND'
        template = '%(function)s(%(expressions)s, 2)'

    queryset = Author.objects.prefetch_related('book_set').annotate(average_rating=Round(Avg('book__rating')))


class BookListView(generic.ListView):
    model = Book
    paginate_by = 25


class BookDetailView(generic.DetailView):
    queryset = Book.objects.select_related("publisher").prefetch_related('authors', 'store_set')


class PublisherListView(generic.ListView):
    queryset = Publisher.objects.all().prefetch_related('book_set').annotate(books_count=Count('book'))
    paginate_by = 25


class PublisherDetailView(generic.DetailView):
    queryset = Publisher.objects.all().prefetch_related('book_set').annotate(books_count=Count('book'))


class StoreListView(generic.ListView):
    queryset = Store.objects.all().prefetch_related('books').annotate(books_count=Count('books'))
    paginate_by = 25


class StoreDetailView(generic.DetailView):
    queryset = Store.objects.all().prefetch_related('books')
