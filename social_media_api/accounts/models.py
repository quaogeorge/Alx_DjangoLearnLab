from django.db import models
from django.contrib.auth.models import AbstractUser

def profile_image_upload_path(instance, filename):
    return f'profiles/{instance.username}/{filename}'

class User(AbstractUser):
    # keep username, email, password from AbstractUser
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to=profile_image_upload_path, blank=True, null=True)
    # followers - many-to-many to self (asymmetric relation)
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='following',
        blank=True
    )

    def __str__(self):
        return self.username