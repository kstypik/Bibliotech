from autoslug import AutoSlugField
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from="title")
    isbn = models.CharField(max_length=13)
    cover_image = models.ImageField(upload_to="book-covers/")
    first_release = models.DateField()
    description = models.TextField()
    publisher = models.ForeignKey("Publisher", on_delete=models.CASCADE)
    authors = models.ManyToManyField("BookAuthor")

    def __str__(self):
        return self.title


class BookAuthor(models.Model):
    name = models.CharField(max_length=80)
    slug = AutoSlugField(populate_from="name")
    photo = models.ImageField(upload_to="author-photos/")
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)
    birthplace = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    twitter_username = models.CharField(max_length=15, blank=True)
    # TODO: wikipedia?

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="name")
    website = models.URLField(blank=True)
    logo = models.ImageField(upload_to="publisher-logo/")
    description = models.TextField()

    def __str__(self):
        return self.name
