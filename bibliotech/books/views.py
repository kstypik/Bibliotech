from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Book, BookAuthor, BookRecord, Publisher
from .serializers import (
    BookAuthorSerializer,
    BookDetailSerializer,
    BookListSerializer,
    BookReadingStatusListSerializer,
    BookReadingStatusSerializer,
    PublisherSerializer,
)


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


class PublisherDetailView(generics.RetrieveAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    lookup_field = "slug"


class BookReadingStatusRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = BookReadingStatusSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return BookRecord.objects.filter(user=self.request.user)

    def get_object(self):
        book = generics.get_object_or_404(Book, slug=self.kwargs["book_slug"])
        obj, _ = BookRecord.objects.get_or_create(
            user=self.request.user,
            book=book,
        )
        self.check_object_permissions(self.request, obj)
        return obj


class BookReadingStatusListView(generics.ListAPIView):
    serializer_class = BookReadingStatusListSerializer

    def get_queryset(self):
        return BookRecord.objects.filter(user=self.request.user)
