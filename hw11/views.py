from abc import ABC
from datetime import datetime, timedelta

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Avg, Count, Func
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.cache import cache_page

from .forms import ReminderForm
from .models import Author, Book, Publisher, Store
from .tasks.reminder_task import reminder


class Round(Func, ABC):
    function = 'ROUND'
    template = '%(function)s(%(expressions)s, 2)'


@method_decorator(cache_page(30), name='dispatch')
class IndexTemplateView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_authors'] = Author.objects.count()
        context['num_books'] = Book.objects.count()
        context['num_publishers'] = Publisher.objects.count()
        context['num_stores'] = Store.objects.count()
        return context


@method_decorator(cache_page(30), name='dispatch')
class AuthorListView(generic.ListView):
    queryset = Author.objects.all().prefetch_related('book_set').annotate(books_count=Count('book'))
    paginate_by = 25


class AuthorDetailView(generic.DetailView):
    queryset = Author.objects.prefetch_related('book_set').annotate(average_rating=Round(Avg('book__rating')))


class AuthorCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Author
    template_name = 'hw13/author_form.html'
    fields = '__all__'
    success_message = 'Author successfully created'
    success_url = reverse_lazy('author-list')
    login_url = '/admin/'


class AuthorUpdateView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Author
    template_name = 'hw13/author_form.html'
    fields = '__all__'
    success_message = 'Author successfully updated'
    success_url = reverse_lazy('author-list')
    login_url = '/admin/'


class AuthorDeleteView(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = Author
    template_name = 'hw13/author_confirm_delete.html'
    success_message = 'Author successfully deleted'
    success_url = reverse_lazy('author-list')
    login_url = '/admin/'


@method_decorator(cache_page(30), name='dispatch')
class BookListView(generic.ListView):
    model = Book
    paginate_by = 25


class BookDetailView(generic.DetailView):
    queryset = Book.objects.select_related("publisher").prefetch_related('authors', 'store_set')


class BookCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Book
    template_name = 'hw13/book_form.html'
    fields = '__all__'
    success_message = 'Book successfully created'
    success_url = reverse_lazy('book-list')
    login_url = '/admin/'


class BookUpdateView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Book
    template_name = 'hw13/book_form.html'
    fields = '__all__'
    success_message = 'Book successfully updated'
    success_url = reverse_lazy('book-list')
    login_url = '/admin/'


class BookDeleteView(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = Book
    template_name = 'hw13/book_confirm_delete.html'
    success_message = 'Book successfully deleted'
    success_url = reverse_lazy('book-list')
    login_url = '/admin/'


@method_decorator(cache_page(30), name='dispatch')
class PublisherListView(generic.ListView):
    queryset = Publisher.objects.all().prefetch_related('book_set').annotate(books_count=Count('book'))
    paginate_by = 25


class PublisherDetailView(generic.DetailView):
    queryset = Publisher.objects.all().prefetch_related('book_set').annotate(books_count=Count('book'))


@method_decorator(cache_page(30), name='dispatch')
class StoreListView(generic.ListView):
    queryset = Store.objects.all().prefetch_related('books').annotate(books_count=Count('books'))
    paginate_by = 25


class StoreDetailView(generic.DetailView):
    queryset = Store.objects.all().prefetch_related('books')


class ReminderFormView(generic.FormView):
    template_name = 'hw12/reminder_form.html'
    form_class = ReminderForm
    success_url = reverse_lazy('reminder-form')

    def get_initial(self):
        initial = super().get_initial()

        initial['date_time'] = f'{(datetime.now() + timedelta(hours=2)).strftime("%Y-%m-%d %H:%M:%S")}'

        return initial

    def form_valid(self, form):
        reminder.apply_async((form.cleaned_data['subject'],
                              form.cleaned_data['date_time'],
                              form.cleaned_data['text'],
                              ), eta=form.cleaned_data['date_time'])
        return super().form_valid(form)
