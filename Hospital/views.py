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




def actualizarmedico(request,idmedico):
    if request.method == "POST":
     if request.POST.get('nombrecompleto') and request.POST.get('email') and request.POST.get('celular') and request.POST.get('direccion') and request.POST.get('edad') and request.POST.get('altura') and request.POST.get('lugar_nacimiento') and request.POST.get('fecha_nacimiento') and request.POST.get('tipo_medico') and request.POST.get('tipo_sangre'):
       medico =Medico.objects.get(id=idmedico)
       medico.NombreCompleto = request.POST.get('nombrecompleto')
       medico.Email = request.POST.get('email')
       medico.Celular= request.POST.get('celular')
       medico.Direccion = request.POST.get('direccion')
       medico.Edad = request.POST.get('edad')
       medico.Altura = request.POST.get('altura')
       medico.Lugar_Nacimiento = request.POST.get('lugar_nacimiento')
       medico.Fecha_Nacimiento = request.POST.get('fecha_nacimiento')
       medico.Tipo_Medico = request.POST.get('tipo_medico')
       medico.Tipo_Sangre = request.POST.get('tipo_sangre')
       medico.save()
       return redirect('/Medico/listado')
    else:
       medico = Medico.objects.filter(id=idmedico)
       return render(request,'Medico/actualizar.html',{'medico':medico})
#endregion



#region Hospital



def insertarhospital(request):
    if request.method == "POST":
     if request.POST.get('nombrehospital') and request.POST.get('direccion') and request.POST.get('ciudad') and request.POST.get('nivel') and request.POST.get('telefono') and request.POST.get('medico_id'):
         #prepare
        insertar = connection.cursor()
        insertar.execute("call insertarhospital('"+request.POST.get ('nombrehospital')+"','"+request.POST.get ('direccion')+"','"+request.POST.get ('ciudad')+"','"+request.POST.get ('nivel')+"','"+request.POST.get ('telefono')+"','"+request.POST.get ('medico_id')+"')")
        return redirect('/Hospital/listado')
    else:
        medicos = Medico.objects.all()
        return render(request,'Hospital/insertar.html',{'medicos':medicos})
#endregion