""" Main URLconf file """
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path("^auth/", include("djoser.urls")),
    re_path(r"^auth/", include("djoser.urls.jwt")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
