from django.urls import path, include

urlpatterns = [
    path("relationship/", include("relationship_app.urls")),
]