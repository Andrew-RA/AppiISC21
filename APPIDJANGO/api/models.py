from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.shortcuts import render
from django.contrib.auth.models import User  # Importa el modelo de usuario predefinido de Django
from django.db import models
from django.contrib.auth.models import User

# CREACIÓN DEL MODELO UserProfile.
class UserProfile(models.Model):
   
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
# feria/models.py


class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()

    def __str__(self):
        return self.user.username

class Atraccion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nombre

class Cotizacion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    atracciones = models.ManyToManyField(Atraccion)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Cotización de {self.cliente.user.username} - {self.fecha_creacion}'

class Venta(models.Model):
    cotizacion = models.OneToOneField(Cotizacion, on_delete=models.CASCADE)
    fecha_venta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Venta de {self.cotizacion.cliente.user.username} - {self.fecha_venta}'

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    atracciones = models.ManyToManyField(Atraccion)

    def __str__(self):
        return self.nombre
    
    
    

