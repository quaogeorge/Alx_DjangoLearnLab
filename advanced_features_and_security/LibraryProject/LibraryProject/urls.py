"""
URL configuration for LibraryProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
"""
from django.urls import path
from .views.admin_view import admin_dashboard
from .views.librarian_view import librarian_dashboard
from .views.member_view import member_dashboard

app_name = "relationship_app"

urlpatterns = [
    path('admin-dashboard/', admin_dashboard, name='admin-dashboard'),
    path('librarian-dashboard/', librarian_dashboard, name='librarian-dashboard'),
    path('member-dashboard/', member_dashboard, name='member-dashboard'),
    path('', include('relationship_app.urls')),
    
]