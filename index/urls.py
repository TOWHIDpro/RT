from urllib.parse import urlparse
from django.urls import path
from .views import IndexView, ServicesView, GalleryView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('service/<slug:slug>', ServicesView.as_view(), name="service"),
    path('gallery', GalleryView.as_view(), name="gallery")
]
