# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    # include custom fields in admin forms
    fieldsets = UserAdmin.fieldsets + (
        ('Extra info', {'fields': ('date_of_birth', 'profile_photo')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Extra info', {'fields': ('date_of_birth', 'profile_photo')}),
    )

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')