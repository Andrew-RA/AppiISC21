from django.shortcuts import render
from rest_framework.views import APIView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


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
        first_name = request.POST.get('primerNombre')
        last_name = request.POST.get('segundoNombre')
        username = request.POST.get('usuario')
        email = request.POST.get('correoElectronico')
        password = request.POST.get('contraseña')
        # Crear un nuevo usuario
        usuario = User.objects.create_user(username=username, password=password)
        usuario.first_name = first_name
        usuario.last_name = last_name
        usuario.email = email
        usuario.save()
        
        # Enviar un correo electrónico con formato HTML y CSS
        subject = 'Registro exitoso'

        # Renderizar el contenido HTML desde una plantilla
        html_content = render_to_string('correo_registro.html', {'username': username, 'first_name': first_name, 'last_name': last_name, 'email': email})

        # Crear una versión de texto sin formato del contenido HTML
        text_content = strip_tags(html_content)

        # Crear el correo electrónico con contenido HTML y texto sin formato
        msg = EmailMultiAlternatives(subject, text_content, 'tu_correo@gmail.com', [email])
        msg.attach_alternative(html_content, "text/html")

        # Enviar el correo electrónico
        msg.send()
        
        
        
        return redirect ('RegistraUsuario') 
    
# clase para darle la bienvenida a un usuario registrado con exito 
class RegistroUser(APIView):
    template_name='correcto.html'
    def get(self,request):
        return render(request,self.template_name)
        
    
class Home(APIView):
    template_name="index.html"
    def get(self,request):
        # Lógica de la vista
        return render(request,self.template_name)
    
    
    
    


