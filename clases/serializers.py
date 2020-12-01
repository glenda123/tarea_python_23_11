from rest_framework import serializers
from clases.models import Clase

class ClaseSerializer(serializers.ModelSerializer):
    created= serializers.DateTimeField(required=False, read_only=True)
    
    class Meta:
        model=Clase
        fields=('nombre', 'horario', 'docente', 'created')
