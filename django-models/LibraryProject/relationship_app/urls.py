from django.urls import path
from . import views
from .views import list_books
from .views import add_book
from .views import edit_book

app_name = 'relationship_app'

urlpatterns = [
    # Function-based view: list all books
    path('books/', views.book_list, name='book_list'),            # if you have a list view
    path('books/<int:pk>/', views.book_detail, name='book_detail'),  # if you have a detail view

    # Class-based view: library detail (expects a primary key)
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),

    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('', views.list_books, name='list_books'), 
    path("add_book/", add_book, name="add_book"),
    path("edit_book", edit_book, name="edit_book")
]
