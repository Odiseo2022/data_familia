from django.shortcuts import render
from django.http import HttpResponse
from webfam.models import datos_familia

# Create your views here.
def inicio(request):
    return HttpResponse("Pagina inicio")

def listar_familia(request):
    data = datos_familia.objects.all()

    return render(request, 'webfam/data_familia.html', {"datos": data})
