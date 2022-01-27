from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexTemplateView.as_view(), name='index'),
    path('authors/', views.AuthorListView.as_view(), name='author-list'),
    path('authors/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('publishers/', views.PublisherListView.as_view(), name='publisher-list'),
    path('publishers/<int:pk>', views.PublisherDetailView.as_view(), name='publisher-detail'),
    path('stores/', views.StoreListView.as_view(), name='store-list'),
    path('stores/<int:pk>', views.StoreDetailView.as_view(), name='store-detail'),
    path('reminder/', views.ReminderFormView.as_view(), name='reminder-form'),

    path('authors/create/', views.AuthorCreateView.as_view(), name='author-create'),
    path('authors/<int:pk>/update/', views.AuthorUpdateView.as_view(), name='author-update'),
    path('authors/<int:pk>/delete/', views.AuthorDeleteView.as_view(), name='author-delete'),

    path('books/create/', views.BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', views.BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book-delete'),

]
