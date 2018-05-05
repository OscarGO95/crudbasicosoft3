from django.db import models

# Create your models here.
class Actividades(models.Model):

    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    fecha_entrega = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    nota = models.IntegerField()