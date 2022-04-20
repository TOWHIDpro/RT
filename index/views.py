from django.shortcuts import render
from django.views import View
from . models import GalleryImages, Focus

# Create your views here.

class IndexView(View):
    def get(self, request):
        gallery_img = GalleryImages.objects.all()
        focus       = Focus.objects.all()

        return render(request, 'index/index.html', {
            'gallery_img': gallery_img,
            'focus'      : focus
        })
