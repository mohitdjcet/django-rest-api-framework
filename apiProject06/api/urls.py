from django.urls import path
from . import views

urlpatterns = [
    path('books/',views.all_books, name='all_books'),
    path('books/select/',views.select_book, name='select_book'),
    path('authors/prefetch/',views.prefetch_authors, name='prefetch_authors'),
]