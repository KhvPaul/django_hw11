from .models import Author, Book, Publisher, Store

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic


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
    model = Author
    paginate_by = 25


class AuthorDetailView(generic.DetailView):
    model = Author

    def author_detail_view(self, pk):
        author = get_object_or_404(Author, pk=pk)
        return render(
            self,
            'hw11/author_detail.html',
            context={'author': author, }
        )


class BookListView(generic.ListView):
    model = Book
    paginate_by = 25


class BookDetailView(generic.DetailView):
    model = Book

    def book_detail_view(self, pk):
        book = get_object_or_404(Book, pk=pk)
        return render(
            self,
            'hw11/book_detail.html',
            context={'book': book, }
        )


class PublisherListView(generic.ListView):
    model = Publisher


class PublisherDetailView(generic.DetailView):
    model = Publisher

    def publisher_detail_view(self, pk):
        publisher = get_object_or_404(Publisher, pk=pk)
        return render(
            self,
            'hw11/publisher_detail.html',
            context={'publisher': publisher, }
        )


class StoreListView(generic.ListView):
    model = Store


class StoreDetailView(generic.DetailView):
    model = Store

    def store_detail_view(self, pk):
        store = get_object_or_404(Store, pk=pk)
        return render(
            self,
            'hw11/store_detail.html',
            context={'store': store, }
        )
