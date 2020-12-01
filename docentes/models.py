from django.db import models




# Create your models here.
class Docente(models.Model) :
    nombre = models.CharField( max_length=100)
    direccion = models.CharField(max_length=120)
    telefono= models.CharField(max_length=20)
    correo=models.CharField(max_length=120)
    created=models.DateTimeField(auto_created=True, null=True)
    updated=models.DateTimeField(auto_now=True, null=True )


    def __str__(self) :
        return self.nombre