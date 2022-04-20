from operator import mod
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Services(models.Model):
    img = models.ImageField(upload_to="services/", help_text = "The image should 600*600")
    title = models.CharField(max_length=50)
    description = RichTextField()

    def __str__(self):
        return self.title