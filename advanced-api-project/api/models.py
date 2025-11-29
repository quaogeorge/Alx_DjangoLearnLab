from django.db import models
from django.utils import timezone

# Author model stores a simple author's name.
# One Author can have many Books (one-to-many relationship).
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Book model stores book details.
# Each Book is linked to one Author via a ForeignKey relationship.
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title