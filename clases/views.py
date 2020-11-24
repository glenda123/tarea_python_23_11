from django.shortcuts import render

# Create your views here.
from clases.models import Clase

def get_clases(request):
    clases= Clase.objects.all()
    return render(request, 'clases/lista.html', {'clases':clases})
    

def get_clase(request, clase_id):
    clase=Clase.objects.get(id=clase_id)
    alumnos=clase.estudiantes.all()
    return render(request, 'clases/detalle.html', {'clase':clase, 'estudiantes':alumnos})