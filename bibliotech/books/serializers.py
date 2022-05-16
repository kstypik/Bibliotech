from rest_framework import serializers

from .models import Book


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
