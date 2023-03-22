"""Hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Hospital.views import insertarmedico,listadomedico,borrarmedico,actualizarmedico
from Hospital.views import insertarhospital,listadohospital,borrarhospital,actualizarhospital
from Hospital.views import insertarusuario,loginusuario,logoutusuario,actualizarusuario,borrarusuario
from Hospital.views import error
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Medico/insertar',insertarmedico),
    path('Medico/listado',listadomedico),
    path('Medico/borrar/<int:idmedico>',borrarmedico),
    path('Medico/actualizar/<int:idmedico>',actualizarmedico),

    path('Hospital/insertar',insertarhospital),
    path('Hospital/listado',listadohospital),
    path('Hospital/borrar/<int:id>',borrarhospital),
    path('Hospital/actualizar/<str:idhospital>',actualizarhospital),

    path('Usuario/insertar',insertarusuario),
    path('Usuario/login',loginusuario),
    path('Usuario/logout',logoutusuario),
    path('Usuario/actualizar/<int:user_id>',actualizarusuario),
    path('Usuario/borrar/<int:user_id>',borrarusuario),

    path('Error/paginaerror',error)



]
