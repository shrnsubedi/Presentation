from django.urls import path, include
from .views import BookList, BookDetail

urlpatterns = [
    path("books/", BookList.as_view()),
    path("books/<int:pk>/", BookDetail.as_view(), name="book_detail"),
]
