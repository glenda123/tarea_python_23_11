from django.db import models
from clases.models import Clase
# Create your models here.

class Estudiante(models.Model):
    nombre=models.CharField(max_length=200)
    edad=models.IntegerField(null=True)
    direccion=models.CharField(max_length=300)
    correo=models.CharField(max_length=200)
    telefono=models.CharField(max_length=20)

    clase=models.ManyToManyField(Clase, related_name='estudiantes')
    created=models.DateTimeField(auto_created=True, null=True)
    updated=models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.nombre