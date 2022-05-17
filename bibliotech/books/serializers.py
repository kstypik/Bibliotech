from rest_framework import serializers

from .models import Book, BookAuthor, BookRecord, Genre, Publisher


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
            "genres",
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


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ["slug", "name", "logo", "website", "description"]


class BookReadingStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookRecord
        fields = ["status"]


class BookReadingStatusListSerializer(serializers.ModelSerializer):
    book = serializers.SlugRelatedField(read_only=True, slug_field="title")
    status = serializers.SerializerMethodField()

    class Meta:
        model = BookRecord
        fields = ["book", "user", "status", "rating"]

    def get_status(self, obj):
        return obj.get_status_display()


class BookRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookRecord
        fields = ["rating"]


class GenreSerializer(serializers.ModelSerializer):
    books = serializers.SlugRelatedField(many=True, read_only=True, slug_field="slug")

    class Meta:
        model = Genre
        fields = ["slug", "name", "description", "books"]


class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["slug", "name"]
