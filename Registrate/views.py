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

