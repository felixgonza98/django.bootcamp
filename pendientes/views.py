from django.shortcuts import render
from django.http import HttpResponse
from pendientes.models import Tarea ##importamos la clase tarea de mode
# Create your views here.

def index(request):
    listita = Tarea.objects.all() ##consultamos la bd y guardamos todos los registros de la tabla tarea como objetos
    saludo = "Hola, Mundo! Esta es la raiz /"
    persona={"nombre":"Marce",
    "edad":33,
    "hobbies":["rugby", "comer pan","cortar patas"],
    "listita_tareas": listita,   ####agregamos la clave listita al diccionario
    }
    return render(request,"inicio.html",persona) #retornamos el saludo

def tarea (request):
    return HttpResponse("Hola soy la vista tarea")

def respuestas(request):
    return HttpResponse("Estas son las respuestas")

def teoria(request):
    return HttpResponse("Estas son todas las teorias")