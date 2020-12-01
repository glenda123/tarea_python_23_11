from django.contrib import admin
from django.urls import path
# from editoriales.views import get_editoriales,
from docentes.views import docentes, docente

app_name='docentes'
urlpatterns = [
    # path('', get_editoriales, name='list'),
    path('', docentes),
    path('<docente_id>/', docente)
]
