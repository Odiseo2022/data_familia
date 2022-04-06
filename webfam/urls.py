from django.urls import path
from webfam.views import *


urlpatterns = [
    path("", inicio),
    path("listarfamilia/", listar_familia),
    
]
