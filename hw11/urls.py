from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('authors/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('publishers/', views.PublisherListView.as_view(), name='publishers'),
    path('publishers/<int:pk>', views.PublisherDetailView.as_view(), name='publisher-detail'),
    path('stores/', views.StoreListView.as_view(), name='stores'),
    path('stores/<int:pk>', views.StoreDetailView.as_view(), name='store-detail'),

]