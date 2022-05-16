from rest_framework import generics

from .models import Book, BookAuthor
from .serializers import BookAuthorSerializer, BookDetailSerializer, BookListSerializer


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()

    def get_serializer_class(self):
        return (
            BookListSerializer if self.request.method == "GET" else BookDetailSerializer
        )


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    lookup_field = "slug"


class BookAuthorDetailView(generics.RetrieveAPIView):
    queryset = BookAuthor.objects.all()
    serializer_class = BookAuthorSerializer
    lookup_field = "slug"
