from django.db import models

# Create your models here.
class Estudiante(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=50)
    grado = models.CharField(max_length=2)