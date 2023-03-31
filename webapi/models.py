from django.db import models

# Create your models here.

class TipoAuto(models.Model):
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion

class Color(models.Model):
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion