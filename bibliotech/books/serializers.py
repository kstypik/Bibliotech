from rest_framework import serializers

from .models import Book, BookAuthor


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["slug", "title", "cover_image"]


class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "slug",
            "title",
            "cover_image",
            "isbn",
            "first_release",
            "description",
            "publisher",
        ]


class BookAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookAuthor
        fields = [
            "slug",
            "name",
            "photo",
            "date_of_birth",
            "date_of_death",
            "birthplace",
            "website",
            "twitter_username",
        ]
