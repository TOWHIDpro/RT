from urllib.parse import urlparse
from django.urls import path
from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name="index")
]
