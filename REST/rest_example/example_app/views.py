from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from .permissions import IsOwnerOrReadOnly
from .filters import IsOwnerFilterBackend

from rest_framework import permissions
from rest_framework import filters


# Create your views here.
class BookList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # ---------
    """
    filter_backends = [IsOwnerFilterBackend, filters.OrderingFilter]
    search_fields = ["title"]
    ordering_fields = ["title"]
    """

    """
    def get_queryset(self):
        return Books.objects.filter(genre=self.kwargs["genre"])
    """


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
