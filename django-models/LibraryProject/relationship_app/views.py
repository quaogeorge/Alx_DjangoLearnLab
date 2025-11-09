from django.views.generic.detail import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'  # Template to render the library details
    context_object_name = 'library'       # Context variable name to use in the template
