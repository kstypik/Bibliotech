from rest_framework import serializers

from .models import Book, BookAuthor, BookRecord, Publisher


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
        fields = ["book", "user", "status"]

    def get_status(self, obj):
        return obj.get_status_display()
