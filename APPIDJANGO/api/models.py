from django.db import models

# NUEVO EXCEL 
class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    correo = models.EmailField()

    def _str_(self):
        return self.nombre
    

# Create your models here.
