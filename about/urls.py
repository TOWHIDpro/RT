from django.urls import path
from . views import AboutView

urlpatterns = [
    path('us', AboutView.as_view(), name="about")
]
