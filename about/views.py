from django.shortcuts import render
from django.views import View
from . models import Employees
# Create your views here.


class AboutView(View):
    def get(self, request):
        employees = Employees.objects.all()
        return render(request, 'about/about.html', {
           'employees': employees 
        })
