from django.db import models

# Create your models here.
class Clase(models.Model):
    nombre=models.CharField(max_length=100)
    horario=models.CharField(max_length=100)
    docente=models.CharField(max_length=150)
    created=models.DateTimeField(auto_created=True, null=True)
    updated=models.DateTimeField(auto_now=True, null=True )

    def __str__(self):
        return self.nombre