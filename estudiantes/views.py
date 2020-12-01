# from django.shortcuts import render

# Create your views here.
from estudiantes.models import Estudiante

# def get_estudiantes(request):
#     estudiantes=Estudiante.objects.all()
#     return render(request, 'estudiantes/lista.html', {'estudiantes':estudiantes})
    

# def get_estudiante(request, estudiante_id):
#     estudiante=Estudiante.objects.get(id=estudiante_id)
#     return render(request, 'estudiantes/detalle.html', {'estudiante':estudiante})

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
# Create your views here.
from django.http import HttpResponse
# Create your views here.
from estudiantes.serializers import EstudianteSerializer



# def get_editoriales(request):
#     response= ''
#     editoriales= Editorial.objects.all()
#     for editorial in editoriales:
#         response += editorial.nombre + ','
#     return HttpResponse(response)

# class EditorialListView(generics.ListCreateAPIView):
#     queryset=Editorial.objects.all()
#     serializer_class=EditorialSerializer

@api_view(['GET', 'POST'])
def estudiantes(request):
    if request.method=='GET':
        estudiantes= Estudiante.objects.all()
        serialized= EstudianteSerializer(estudiantes, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)
    if request.method=='POST':
        estudiante=EstudianteSerializer(data=request.data)
        if estudiante.is_valid():
            estudiante.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=estudiante.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def estudiante(request, estudiante_id):
    estudiante_obj= get_object_or_404(Estudiante, id=estudiante_id)
    
    if request.method=='GET':
        serialized=EstudianteSerializer(estudiante_obj)
        return Response(status=status.HTTP_200_OK, data=serialized.data)
    if request.method=='PUT':
        serialized=EstudianteSerializer(instance=estudiante_obj, data=request.data, partial=True)
        if serialized.is_valid():
            serialized.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serialized.errors)
    if request.method=='DELETE':
        estudiante_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)