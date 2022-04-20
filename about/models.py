from operator import mod
from django.db import models

# Create your models here.

class Employees(models.Model):
    img        = models.ImageField(upload_to="employee/", help_text ="The image should be: 600*600")
    name      = models.CharField(max_length=20)
    short_disc = models.CharField(max_length=50)

    def __str__(self):
        return self.name
