from rest_framework import serializers
from docentes.models import Docente

class DocenteSerializer(serializers.ModelSerializer):
    created= serializers.DateTimeField(required=False, read_only=True)
    
    class Meta:
        model=Docente
        fields=('nombre', 'direccion', 'telefono', 'correo', 'created')
