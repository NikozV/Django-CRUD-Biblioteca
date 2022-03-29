from django.shortcuts import render
#from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm
# Create your views here.

def inicio(request):
    return render (request,'paginas/inicio.html')

def nosotros(request):
    return render (request,'paginas/nosotros.html')

def libros(request):
    libros = Libro.objects.all()
    #print (libros)
    return render (request,'libros/index.html', {'libros': libros})

def crear(request):
    formulario = LibroForm(request.POST or None)
    return render (request,'libros/crear.html', {'formulario': formulario})

def editar (request):
    return render (request,'libros/editar.html')
