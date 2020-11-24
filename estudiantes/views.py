from django.shortcuts import render

# Create your views here.
from estudiantes.models import Estudiante

def get_estudiantes(request):
    estudiantes=Estudiante.objects.all()
    return render(request, 'estudiantes/lista.html', {'estudiantes':estudiantes})
    

def get_estudiante(request, estudiante_id):
    estudiante=Estudiante.objects.get(id=estudiante_id)
    return render(request, 'estudiantes/detalle.html', {'estudiante':estudiante})