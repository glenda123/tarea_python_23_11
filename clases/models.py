from django.db import models
from docentes.models import Docente

# Create your models here.
class Clase(models.Model):
    nombre=models.CharField(max_length=100)
    horario=models.CharField(max_length=100)
    docente=models.ManyToManyField(Docente, related_name='clases' )
    created=models.DateTimeField(auto_created=True, null=True)
    updated=models.DateTimeField(auto_now=True, null=True )
 
    def __str__(self):
        return self.nombre