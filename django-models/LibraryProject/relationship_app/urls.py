from django.urls import path
from . import views

urlpatterns = [
    path('books/add/', views.add_book, name='book-add'),
    path('books/<int:pk>/edit/', views.edit_book, name='book-edit'),
    path('books/<int:pk>/delete/', views.delete_book, name='book-delete'),
    # (Optional) small list/detail views for testing
    path('books/', views.book_list, name='book-list'),
    path('books/<int:pk>/', views.book_detail, name='book-detail'),
]