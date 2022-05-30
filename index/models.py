from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.

class Services(models.Model):
    img = models.ImageField(upload_to="services")
    title = models.CharField(max_length=25)
    desc = RichTextField()
    slug = models.SlugField(null=True, blank=True)
    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Services,self).save(*args,**kwargs)

class Gallery(models.Model):
    img = models.ImageField(upload_to="gallery",  help_text="The image should squire")
    def __str__(self):
        return str(self.img)

class Message(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=80)
    phone = models.CharField(max_length=13)
    message = models.TextField()
    def __str__(self):
        return f"{self.name}|{self.phone}"

