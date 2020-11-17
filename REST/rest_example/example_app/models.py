from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator
from django.contrib.auth import get_user_model

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    isbn = models.PositiveIntegerField(
        null=True, blank=True, validators=[MaxValueValidator(9999999999)]
    )
    description = models.TextField(default="NA")
    genre = models.CharField(max_length=50)
    price = models.PositiveIntegerField(null=True, blank=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("book_detail", args=[str(self.id)])
