from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render,redirect
from Hospital.models import Medico
from django.db import connection
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout


#region Medico


def listadomedico(request):
    paginalistado = open('Hospital/Templates/Medico/listado.html')
    lectura = Template(paginalistado.read())
    paginalistado.close()
    medico = Medico.objects.all()
    parametros = Context({'medico':medico})
    paginafinal = lectura.render(parametros)
    return HttpResponse(paginafinal)


def insertarmedico(request):
    if request.method == "POST":
     if request.POST.get('nombrecompleto') and request.POST.get('email') and request.POST.get('direccion') and request.POST.get('celular') and request.POST.get('edad') and request.POST.get('altura') and request.POST.get('lugar_nacimiento') and request.POST.get('fecha_nacimiento') and request.POST.get('tipo_medico') and request.POST.get('tipo_sangre'):
        medico = Medico()
        medico.NombreCompleto = request.POST.get('nombrecompleto')
        medico.Email = request.POST.get('email')
        medico.Direccion = request.POST.get('direccion')
        medico.Celular= request.POST.get('celular')
        medico.Edad= request.POST.get('edad')
        medico.Altura= request.POST.get('altura')
        medico.Lugar_Nacimiento= request.POST.get('lugar_nacimiento')
        medico.Fecha_Nacimiento= request.POST.get('fecha_nacimiento')
        medico.Tipo_Medico= request.POST.get('tipo_medico')
        medico.Tipo_Sangre= request.POST.get('tipo_sangre')
        medico.save()
        return redirect('/Medico/listado')
    else:
        return render(request,'Medico/insertar.html')


def borrarmedico(request,idmedico):
    medico = Medico.objects.get(id=idmedico)
    medico.delete()
    return redirect('/Medico/listado')





#endregion


