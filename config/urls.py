from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("main.urls", namespace="main")),
    path('catalog/', include('products.urls', namespace="catalog")),
    path("about/", include("about.urls", namespace="about")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)