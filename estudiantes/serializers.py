from rest_framework import serializers
from estudiantes.models import Estudiante

class EstudianteSerializer(serializers.ModelSerializer):
    created= serializers.DateTimeField(required=False, read_only=True)
    
    class Meta:
        model=Estudiante
        fields=('nombre', 'edad', 'direccion', 'correo', 'telefono', 'clase', 'created')