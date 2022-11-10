from django.http import HttpResponse
from appcoder.models import Curso
from django.shortcuts import render


def inicio(request):
    return render(request, "appcoder/index.html")

def cursos(request):
    #obtenemos el listado de objetos de la base de datos
    #cursos = Curso.objects.all()

    #for curso in cursos:
     #   print(curso.nombre)

    return render(request, "appcoder/cursos.html")

def creacion_curso(request):
    if request.method == "POST":
        nombre_curso = request.POST["curso"]
        numero_camada = int(request.POST["camada"])

        curso = Curso(nombre=nombre_curso, camada=numero_camada)
        curso.save()
        
    return render(request, "appcoder/curso_formulario.html" )

    
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
