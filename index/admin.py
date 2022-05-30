from telnetlib import GA
from django.contrib import admin
from . models import Message, Services, Gallery
# Register your models here.



admin.site.register(Message)
admin.site.register(Gallery)

@admin.register(Services)
class AuthorAdmin(admin.ModelAdmin):
    fields = ('img', 'title', 'desc')