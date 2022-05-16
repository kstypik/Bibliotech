from django.urls import path

from . import views

urlpatterns = [
    path("", views.BookListCreateView.as_view(), name="book_list"),
    path("<slug:slug>/", views.BookDetailView.as_view(), name="book_detail"),
]
