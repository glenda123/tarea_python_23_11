# from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
# Create your views here.
from django.http import HttpResponse
# Create your views here.
from docentes.serializers import DocenteSerializer

from docentes.models import Docente

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
def docentes(request):
    if request.method=='GET':
        docentes= Docente.objects.all()
        serialized= DocenteSerializer(docentes , many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)
    if request.method=='POST':
        docente=DocenteSerializer(data=request.data)
        if docente.is_valid():
            docente.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=docente.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def docente(request, docente_id):
    docente_obj= get_object_or_404(Docente, id=docente_id)
    
    if request.method=='GET':
        serialized=DocenteSerializer(docente_obj)
        return Response(status=status.HTTP_200_OK, data=serialized.data)
    if request.method=='PUT':
        serialized=DocenteSerializer(instance=docente_obj, data=request.data, partial=True)
        if serialized.is_valid():
            serialized.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serialized.errors)
    if request.method=='DELETE':
        docente_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)