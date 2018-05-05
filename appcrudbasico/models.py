from django.db import models

# Create your models here.
class Materia(models.Model):
    nombre = models.CharField(max_length=30)
    profesor = models.CharField(max_length=30)
    intensidad = models.IntegerField()