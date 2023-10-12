from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.shortcuts import render
from django.contrib.auth.models import User  # Importa el modelo de usuario predefinido de Django


# CREACIÓN DEL MODELO UserProfile.
class UserProfile(models.Model):
   
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    

