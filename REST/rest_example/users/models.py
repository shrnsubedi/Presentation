from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager

# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=10)
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    phone = models.PositiveIntegerField(null=True, blank=True)
    address = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse("login")

    def __str__(self):
        return self.email