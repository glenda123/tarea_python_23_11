
from django.contrib import admin
from django.urls import path
# from editoriales.views import get_editoriales,
from clases.views import clases, clase

app_name='clases'
urlpatterns = [
    # path('', get_editoriales, name='list'),
    path('', clases),
    path('<clase_id>/', clase)
]
