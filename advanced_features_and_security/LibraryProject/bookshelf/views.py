from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required, login_required
from django.urls import reverse
from .models import Book
from .forms import BookForm
from .forms import ExampleForm

from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect, render

@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
@require_http_methods(["GET", "POST"])
def book_create(request):
    # use BookForm (ModelForm) for validation
    ...



# List view: require can_view
@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# Create view: require can_create
@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.created_by = request.user
            book.save()
            return redirect(reverse('bookshelf:book_list'))
    else:
        form = BookForm()
    return render(request, 'bookshelf/book_form.html', {'form': form})

# Edit view: require can_edit
@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect(reverse('bookshelf:book_list'))
    return render(request, 'bookshelf/book_form.html', {'form': form, 'book': book})

# Delete view: require can_delete
@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect(reverse('bookshelf:book_list'))
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})

from django.db.models import Q
from django.shortcuts import render
from .forms import BookSearchForm
from .models import Book

def book_search(request):
    form = BookSearchForm(request.GET or None)
    books = Book.objects.none()
    if form.is_valid():
        q = form.cleaned_data.get('q') or ''
        # use ORM with parameterization (no string formatting)
        books = Book.objects.filter(
            Q(title__icontains=q) | Q(author__icontains=q)
        )
    return render(request, 'bookshelf/book_search.html', {'form': form, 'books': books})

from .forms import SearchForm
from django.db.models import Q
from django.shortcuts import render

def search_books(request):
    form = SearchForm(request.GET or None)
    books = []

    if form.is_valid():
        q = form.cleaned_data['q']
        books = Book.objects.filter(
            Q(title__icontains=q) |
            Q(author__icontains=q)
        )

    return render(request, 'bookshelf/search_books.html', {
        'form': form,
        'books': books
    })