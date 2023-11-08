from django.shortcuts import render
from DjangoAplicacion.models import Curso
from django.http import HttpResponse

# Create your views here.
def curso (self):
    curso = Curso(nombre = "Python", camada = 56858)
    curso.save()
    documento = f"------> Curso {curso.nombre}, Camada {curso.camada}"
    return HttpResponse(documento)

def inicio(request):
    return render(request, "DjangoAplicacion/inicio.html")

def index(request):
    return render(request, "DjangoAplicacion/index.html")

def padre(request):
    return render(request, "DjangoAplicacion/padre.html")

def cursos(request):
    return render(request, "DjangoAplicacion/cursos.html")

def profesores(request):
    return render(request, "DjangoAplicacion/profesores.html")

def estudiantes(request):
    return render(request, "DjangoAplicacion/estudiantes.html")

def entregables(request):
    return render(request, "DjangoAplicacion/entregables.html")

def cursos_form(request):
    if request.method == 'POST':
        curso = Curso(request.POST['curso'], request.POST['camada'])
        curso.save()
        return render(request, "DjangoAplicacion/inicio.html")
    return render(request, "DjangoAplicacion/cursos_formulario.html")
    