from django.contrib.auth.models import AbstractUser
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class User(AbstractUser):
    class Role(models.TextChoices):
        admin = "ADMIN", "Admin"
        user = "USER", "User"

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.user)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    bio = CKEditor5Field('Bio',blank=True,)
    job = models.CharField(max_length=100, blank=True, null=True)
    resume = models.FileField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return f"{self.username}"
