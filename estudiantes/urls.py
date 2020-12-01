from django.contrib import admin
from django.urls import path
# from editoriales.views import get_editoriales,
from estudiantes.views import estudiantes, estudiante

app_name='estudiantes'
urlpatterns = [
    # path('', get_editoriales, name='list'),
    path('', estudiantes),
    path('<estudiante_id>/', estudiante)
]
