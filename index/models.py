from django.db import models

# Create your models here.

class GalleryImages(models.Model):
    img = models.ImageField(upload_to="gallery/",  help_text="The image should squire")
    def __str__(self):
        return str(self.img)

class Focus(models.Model):
    icon = models.CharField(max_length=30, help_text="Give icons like this: icofont-bars")
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Message(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=80)
    phone = models.CharField(max_length=13)
    message = models.TextField()
    def __str__(self):
        return f"{self.name}|{self.phone}"