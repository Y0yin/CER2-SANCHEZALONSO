from django.shortcuts import render
from django.http import HttpResponse
from .models import Comunicado, Entidad
# Create your views here.

def filtro(request):
    departamento = request.GET.get('departamento')
    comunicados = []

    if departamento == "Departamento":
        comunicados = Comunicado.objects.all().order_by('-fecha_publicacion')  # Ordenar por fecha_publicación de forma descendente
    elif departamento:
        comunicados = Comunicado.objects.filter(entidad__nombre=departamento).order_by('-fecha_publicacion')
    
    entidades = Entidad.objects.all()
    
    data = {
        "comunicados": comunicados,
        "entidades": entidades,
    }
    
    return render(request, 'blog/base.html', data)

