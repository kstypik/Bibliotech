from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Book, BookAuthor, BookRecord, Genre, Publisher
from .serializers import (
    BookAuthorSerializer,
    BookDetailSerializer,
    BookListSerializer,
    BookRatingSerializer,
    BookReadingStatusListSerializer,
    BookReadingStatusSerializer,
    GenreListSerializer,
    GenreSerializer,
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


class BookRecordRetrieveUpdateBaseView(generics.RetrieveUpdateAPIView):
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


class BookReadingStatusRetrieveUpdateView(BookRecordRetrieveUpdateBaseView):
    serializer_class = BookReadingStatusSerializer
    permission_classes = (IsAuthenticated,)


class BookReadingStatusListView(generics.ListAPIView):
    serializer_class = BookReadingStatusListSerializer

    def get_queryset(self):
        return BookRecord.objects.filter(user=self.request.user)


class BookRatingRetrieveUpdateView(BookRecordRetrieveUpdateBaseView):
    serializer_class = BookRatingSerializer
    permission_classes = (IsAuthenticated,)


class GenreRetrieveView(generics.RetrieveAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    lookup_field = "slug"
    lookup_url_kwarg = "slug"


class GenreListView(generics.ListAPIView):
    serializer_class = GenreListSerializer
    queryset = Genre.objects.all()
