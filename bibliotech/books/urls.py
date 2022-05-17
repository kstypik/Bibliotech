from django.urls import path

from . import views

urlpatterns = [
    path("", views.BookListCreateView.as_view(), name="book_list"),
    path("status/", views.BookReadingStatusListView.as_view(), name="status_list"),
    path("<slug:slug>/", views.BookDetailView.as_view(), name="book_detail"),
    path(
        "<slug:book_slug>/status/",
        views.BookReadingStatusRetrieveUpdateView.as_view(),
        name="book_status_retrieve_update",
    ),
    path(
        "<slug:book_slug>/rating/",
        views.BookRatingRetrieveUpdateView.as_view(),
        name="book_rating_retrieve_update",
    ),
]
