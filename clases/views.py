# from django.shortcuts import render

# Create your views here.
# from clases.models import Clase

# def get_clases(request):
#     clases= Clase.objects.all()
#     return render(request, 'clases/lista.html', {'clases':clases})
    

# def get_clase(request, clase_id):
#     clase=Clase.objects.get(id=clase_id)
#     alumnos=clase.estudiantes.all()
#     return render(request, 'clases/detalle.html', {'clase':clase, 'estudiantes':alumnos})




from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
# Create your views here.
from django.http import HttpResponse
# Create your views here.
from clases.serializers import ClaseSerializer

from clases.models import Clase

# def get_editoriales(request):
#     response= ''
#     editoriales= Editorial.objects.all()
#     for editorial in editoriales:
#         response += editorial.nombre + ','
#     return HttpResponse(response)

# class ClaseListView(generics.ListCreateAPIView):
#     queryset=Clase.objects.all()
#     serializer_class=ClaseSerializer

@api_view(['GET', 'POST'])
def clases(request):
    if request.method=='GET':
        clases= Clase.objects.all()
        serialized= ClaseSerializer(clases , many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)
    if request.method=='POST':
        clase=ClaseSerializer(data=request.data)
        if clase.is_valid():
            clase.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=clase.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def clase(request, clase_id):
    clase_obj= get_object_or_404(Clase, id=clase_id)
    
    if request.method=='GET':
        serialized=ClaseSerializer(clase_obj)
        return Response(status=status.HTTP_200_OK, data=serialized.data)
    if request.method=='PUT':
        serialized=ClaseSerializer(instance=clase_obj, data=request.data, partial=True)
        if serialized.is_valid():
            serialized.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serialized.errors)
    if request.method=='DELETE':
        clase_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)