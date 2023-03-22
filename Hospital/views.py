from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render,redirect
from Hospital.models import Medico
from Hospital.models import Hospital
from django.db import connection
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#region Medico


def listadomedico(request):
    if not request.user.is_authenticated:
        return redirect('/Usuario/login')
    paginalistado = open('Hospital/Templates/Medico/listado.html')
    lectura = Template(paginalistado.read())
    paginalistado.close()
    medico = Medico.objects.all()
    parametros = Context({'medico':medico})
    paginafinal = lectura.render(parametros)
    return HttpResponse(paginafinal)


def insertarmedico(request):
    if not request.user.is_authenticated:
        return redirect('/Usuario/login')
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
    if not request.user.is_authenticated:
        return redirect('/Usuario/login')
    if request.method == "POST":
     if request.POST.get('nombrehospital') and request.POST.get('direccion') and request.POST.get('ciudad') and request.POST.get('nivel') and request.POST.get('telefono') and request.POST.get('medico_id'):
         #prepare
        insertar = connection.cursor()
        insertar.execute("call insertarhospital('"+request.POST.get ('nombrehospital')+"','"+request.POST.get ('direccion')+"','"+request.POST.get ('ciudad')+"','"+request.POST.get ('nivel')+"','"+request.POST.get ('telefono')+"','"+request.POST.get ('medico_id')+"')")
        return redirect('/Hospital/listado')
    else:
        medicos = Medico.objects.all()
        return render(request,'Hospital/insertar.html',{'medicos':medicos})
    




def listadohospital(request):
    if not request.user.is_authenticated:
        return redirect('/Usuario/login') 
    listado = connection.cursor()
    listado.execute("call listadohospital")
    return render(request, 'Hospital/listado.html', {'hospital': listado})




def borrarhospital(request,id):
    with connection.cursor() as cursor:
        cursor.callproc('borrarhospital', [id])
    return redirect('/Hospital/listado')


def actualizarhospital(request,idhospital):
     if request.method =="POST":
        if request.POST.get('nombrehospital') and request.POST.get('direccion') and request.POST.get('ciudad') and request.POST.get('nivel') and request.POST.get('telefono') and request.POST.get('medico_id'):
            hospital = Hospital.objects.get(id=idhospital)
            actualizar = connection.cursor()
            actualizar.execute("call actualizarhospital('" + idhospital +"', '"+ request.POST.get('nombrehospital')  +"','"
            +  request.POST.get('direccion') +"','" + request.POST.get('ciudad') +"','" + request.POST.get('nivel') +"','" + request.POST.get('telefono') +"','" + request.POST.get('medico_id') +"') ")
            return redirect('/Hospital/listado')
     else:
        medicos = Medico.objects.all()
        hospital = Hospital.objects.filter(id=idhospital)
        return render(request, 'Hospital/actualizar.html', {'hospital' : hospital, 'medicos' : medicos})


  
#endregion



#region usuario
def insertarusuario(request):
    if request.method == "POST":
     if request.POST.get('username') and request.POST.get('password') and request.POST.get('nombres') and request.POST.get('apellidos') and request.POST.get('email') :
        
        usuario = User.objects.create_user(username=request.POST.get('username'),email=request.POST.get('email'),password=request.POST.get('password'),first_name= request.POST.get('nombres'),last_name=request.POST.get('apellidos') )
      
         
        usuario.save()
        return redirect('/Usuario/login')
    else:
        return render(request,'Usuario/insertar.html')
    





def loginusuario(request):
    if request.method == "POST":
     if request.POST.get('username') and request.POST.get('password'):
        user = authenticate(username= request.POST.get('username'),password= request.POST.get('password'))  
        if user is not None:
           login(request,user)
           return redirect('/Medico/insertar')
        else:
           mensaje = "Usuario  o Cotraseña incorrecta,Intenta de Nuevo"
           return render(request,'Usuario/login.html',{'mensaje':mensaje})
    else:
        return render(request,'Usuario/login.html')




def logoutusuario(request):
    logout(request)
    return redirect('/Usuario/login')
 

def actualizarusuario(request, user_id):
    user = request.user
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('password') and request.POST.get('nombres') and request.POST.get('apellidos') and request.POST.get('email'):
            user= User.objects.get(id=user_id)
            user.username = request.POST.get('username')
            user.password = request.POST.get('password')
            user.first_name = request.POST.get('nombres')
            user.last_name = request.POST.get('apellidos')
            user.email = request.POST.get('email')
            user.save()
            #mensaje cuando actualice los datos
            messages.success(request, 'Datos actualizados correctamente.')
            return redirect(f"/Usuario/actualizar/{user.id}")
    else:
        # verificar si el usuario en sesión coincide con el usuario que se está actualizando
        if str(user.id) != str(user_id):
            # si no coincide, redireccionar al usuario a una página de error o a la página de inicio
            return redirect('/Usuario/login')
        else:
            user= User.objects.filter(id=user_id)
            return render(request, 'Usuario/actualizar.html', {'user': user})

    



def borrarusuario(request,user_id):
    medico = User.objects.get(id=user_id)
    medico.delete()
    return redirect('/Usuario/insertar')

#endregion