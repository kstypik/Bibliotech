from django.contrib import admin

from .models import Book, BookAuthor, BookRecord, Publisher

admin.site.register(Book)
admin.site.register(BookAuthor)
admin.site.register(Publisher)
admin.site.register(BookRecord)
