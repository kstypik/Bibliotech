import os

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from autoslug import AutoSlugField

from bibliotech.users.models import User


def book_covers_path(instance, filename):
    extension = os.path.splitext(filename)[1]
    return f"book-covers/{instance.slug}{extension}"


def author_photos_path(instance, filename):
    extension = os.path.splitext(filename)[1]
    return f"author-photos/{instance.slug}{extension}"


def publisher_logos_path(instance, filename):
    extension = os.path.splitext(filename)[1]
    return f"publisher-logos/{instance.slug}{extension}"


class Book(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from="title")
    isbn = models.CharField(max_length=13)
    cover_image = models.ImageField(upload_to=book_covers_path)
    first_release = models.DateField()
    description = models.TextField()
    page_count = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1), MaxValueValidator(25_000)],
    )
    publisher = models.ForeignKey("Publisher", on_delete=models.CASCADE)
    authors = models.ManyToManyField("BookAuthor")
    genres = models.ManyToManyField("Genre", related_name="books")

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_page_count_range",
                check=models.Q(page_count__range=(1, 25_000)),
            ),
        ]

    def __str__(self):
        return self.title


class BookAuthor(models.Model):
    name = models.CharField(max_length=80)
    slug = AutoSlugField(populate_from="name")
    photo = models.ImageField(upload_to=author_photos_path)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)
    birthplace = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    twitter_username = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(populate_from="name")
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="name")
    website = models.URLField(blank=True)
    logo = models.ImageField(upload_to=publisher_logos_path)
    description = models.TextField()

    def __str__(self):
        return self.name


class BookRecord(models.Model):
    class Status(models.TextChoices):
        READ = "R", _("Read")
        CURRENTLY_READING = "CR", _("Currently Reading")
        WANT_TO_READ = "WR", _("Want to Read")

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=Status.choices)
    rating = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )
    pages_read = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1), MaxValueValidator(25_000)],
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_rating_range",
                check=models.Q(rating__range=(1, 5)),
            ),
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_pages_read_range",
                check=models.Q(pages_read__range=(1, 25_000)),
            ),
        ]
