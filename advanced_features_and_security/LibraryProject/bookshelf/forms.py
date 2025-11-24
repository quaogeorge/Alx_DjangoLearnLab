from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'date_of_birth', 'profile_photo')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'date_of_birth', 'profile_photo', 'is_active', 'is_staff', 'is_superuser')


from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']   

from django import forms

class BookSearchForm(forms.Form):
    q = forms.CharField(required=False, max_length=200)    

from django import forms

class SearchForm(forms.Form):
    q = forms.CharField(max_length=100, required=False)             