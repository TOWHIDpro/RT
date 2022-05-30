from django.shortcuts import render
from django.views import View
from . models import Services, Gallery

# Create your views here.

class IndexView(View):
    def get(self, request):
        services = Services.objects.all()
        return render(request, 'index/index.html', {
            'services': services,
        })

class ServicesView(View):
    def get(self, request, slug):
        service = Services.objects.get(slug=slug)
        return render(request, 'index/service.html', {
            'service': service
        })

class GalleryView(View):
    def get(self, request):
        gallery = Gallery.objects.all()
        return render(request, 'index/gallery.html', {
            'gallery': gallery
        })
