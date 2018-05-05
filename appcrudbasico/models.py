from django.db import models

# Create your models here.
class Maestros(models.Model):

    cedula = models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    materia = models.CharField(max_length=100)