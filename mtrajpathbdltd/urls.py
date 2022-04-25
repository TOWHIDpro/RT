from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('about', include('about.urls')),
    path('services', include('services.urls')),
    path('contact', include('contact.urls')),

    # API's
    path('api/index/', include('index.api.urls')),
    path('api/services/', include('services.api.urls'))
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
