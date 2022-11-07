from django.http import HttpResponse
from appcoder.models import Curso
from django.shortcuts import render


def inicio(request):
    return render(request, "appcoder/index.html")


def cursos(request):
    return HttpResponse("Estas en cursos")
    
def estudiantes(request):
    return HttpResponse("Estas en estudiantes")

def profesores(request):
    return HttpResponse("Estas en profesores")

def entregables(request):
    return HttpResponse("Estas en entregables")

# def listado_cursos(request):
#     cursos = Curso.objects.all()

#     # Respuesta casera
#     cadena_respuesta = "<ul>"
#     for curso in cursos:
#         cadena_respuesta += f"<li>({curso.nombre},{curso.camada}) </li>"
#     cadena_respuesta += "</ul>"

#     return HttpResponse(cadena_respuesta)
