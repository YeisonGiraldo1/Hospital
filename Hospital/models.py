from django.db import models

class Medico(models.Model):
    NombreCompleto = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Celular = models.CharField(max_length=255)
    Direccion = models.CharField(max_length=255)
    Edad = models.CharField(max_length=255)
    Altura = models.CharField(max_length=255)
    Lugar_Nacimiento = models.CharField(max_length=255)
    Fecha_Nacimiento = models.CharField(max_length=255)
    Tipo_Medico = models.CharField(max_length=255)
    Tipo_Sangre = models.CharField(max_length=255)
    class Meta:
      db_table = 'medico'