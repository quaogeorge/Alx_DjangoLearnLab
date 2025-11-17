from django.urls import path
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path('admin-view/', admin_view, name='admin-view'),
    path('librarian-view/', librarian_view, name='librarian-view'),
    path('member-view/', member_view, name='member-view'),
]