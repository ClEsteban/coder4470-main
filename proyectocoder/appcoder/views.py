from django.http import HttpResponse
from appcoder.models import Curso
from django.shortcuts import render


def inicio(request):
    return render(request, "appcoder/index.html")

def cursos(request):
    return render(request, "appcoder/cursos.html")
    
def estudiantes(request):
    return render(request, "appcoder/estudiantes.html")

def profesores(request):
    return render(request, "appcoder/profesores.html")

def entregables(request):
        return render(request, "appcoder/entregables.html")


# def listado_cursos(request):
#     cursos = Curso.objects.all()

#     # Respuesta casera
#     cadena_respuesta = "<ul>"
#     for curso in cursos:
#         cadena_respuesta += f"<li>({curso.nombre},{curso.camada}) </li>"
#     cadena_respuesta += "</ul>"

#     return HttpResponse(cadena_respuesta)
