from django.shortcuts import render, redirect
from .models import nombre
# Create your views here.
def login(request):
    Nombre = nombre.objects.all()
    return render(request, 'login.html', {"Nombre": Nombre })

def create_nombre(request):
    Nombre = nombre(nombre=request.POST['nombre'], apellido=request.POST['apellido'], ciudad=request.POST['ciudad'])
    Nombre.save()
    return redirect('/Registrate/')

def delete_dato(request, Nombre_id):
    Nombre = nombre.objects.get(id=Nombre_id)
    Nombre.delete()
    return redirect('/Registrate/')

def editar_dato(request, Nombre_id):
    Nombre = nombre.objects.get(id = Nombre_id)
    if request.method == "POST":
        
        Nombre.nombre   = request.POST['nombre']
        Nombre.apellido = request.POST['apellido']
        Nombre.ciudad   = request.POST['ciudad']
        Nombre.save()
        return redirect('/Registrate/')
        
    return render(request, 'editar.html', {"Nombre": Nombre })
 
