from django.shortcuts import render
from django.views import View
from . models import Services
# Create your views here.

class ServicesView(View):
    def get(self, request):
        services = Services.objects.all()
        return render(request, 'services/services.html', {
            'services': services
        })
