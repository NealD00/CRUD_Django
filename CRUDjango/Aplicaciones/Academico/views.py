from django.shortcuts import render, redirect
from .models import Curso
from django.contrib import messages


def home(request):
    cursoslistados = Curso.objects.all()
    return render(request, "gestioncursos.html", {"cursos": cursoslistados})

def registrarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    apellido=request.POST['txtApellido']
    email=request.POST['txtEmail']
    fechaNacimiento=request.POST['txtfechaNacimiento']
    #creditos=request.POST['numCreditos']

    #curso=Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
    curso=Curso.objects.create(codigo=codigo, nombre=nombre, apellido=apellido, email=email, fechaNacimiento=fechaNacimiento)
    messages.success(request,'!Alumno Asignados!')
    return redirect('/')

def edicionCurso(request,codigo):
    curso = Curso.objects.get(codigo=codigo)
    messages.success(request,'!Cursos Editado!')
    return render(request, "edicionCurso.html",{"curso": curso})

def editarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    apellido=request.POST['txtApellido']
    email=request.POST['txtEmail']
    fechaNacimiento=request.POST['txtfechaNacimiento']

    #creditos=request.POST['numCreditos']

    curso=Curso.objects.get(codigo=codigo) #nombre=nombre, apellido=apellido, email=email, fechaNacimiento=fechaNacimiento)
    curso.nombre = nombre
    curso.apellido = apellido
    curso.email = email
    curso.fechaNacimiento= fechaNacimiento
    #curso.creditos = creditos
    curso.save()
    
    messages.success(request,'!Cursos Actualizado!')
    return redirect('/')



def eliminarCurso(request,codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    messages.success(request,'!Alumno Eliminado!')
    return redirect('/')

