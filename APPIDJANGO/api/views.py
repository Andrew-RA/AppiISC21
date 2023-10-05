from django.shortcuts import render
from rest_framework.views import APIView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from rest_framework.views import APIView



class Login(APIView):
    template_name="login.html"
    def get(self,request):
        # Lógica de la vista
        return render(request,self.template_name)
    

class RegistraUsuario(APIView):
    template_name="register.html"
    def get(self,request):
        # Lógica de la vista
        return render(request,self.template_name)
    
    def post(self, request):
        # Obtener datos del formulario POST
        username = request.POST.get('usuario')
        password = request.POST.get('contraseña')
        first_name = request.POST.get('primerNombre')
        last_name = request.POST.get('segundoNombre')
        email = request.POST.get('correoElectronico')
        
    # Crear un nuevo usuario
        usuario = User.objects.create_user(username=username, password=password)
        usuario.first_name = first_name
        usuario.last_name = last_name
        usuario.email = email
        usuario.save()

    
class Home(APIView):
    template_name="index.html"
    def get(self,request):
        # Lógica de la vista
        return render(request,self.template_name)



