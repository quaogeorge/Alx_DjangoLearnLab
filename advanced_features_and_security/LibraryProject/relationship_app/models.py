from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# ---------------------------------------------------
#  CUSTOM USER MANAGER
# ---------------------------------------------------
class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self.create_user(email, password, **extra_fields)


# ---------------------------------------------------
#  CUSTOM USER MODEL
# ---------------------------------------------------
class CustomUser(AbstractUser):
    # Remove username field
    username = None

    # Use email as the unique identifier
    email = models.EmailField(unique=True)

    # New custom fields
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []   # we removed username

    objects = CustomUserManager()

    def __str__(self):
        return self.email