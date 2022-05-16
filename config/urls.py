""" Main URLconf file """
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

from bibliotech.books import views

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path("^auth/", include("djoser.urls")),
    re_path(r"^auth/", include("djoser.urls.jwt")),
    path("books/", include("bibliotech.books.urls")),
    path(
        "authors/<slug:slug>/",
        views.BookAuthorDetailView.as_view(),
        name="book_author_detail",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
