from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views import View
from django.shortcuts import redirect
import random
import string
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
import random
import string
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.http import HttpResponse
import xlsxwriter



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
        
        
        
        return redirect ('Home') 
    
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
    
# clase para visualuzar usuarios registrados
class UserListView(ListView):
    model = User
    template_name = 'user_list.html'  # Nombre de la plantilla HTML
    context_object_name = 'users'  # Nombre de la variable en la plantilla que contendrá la lista de usuarios
    
class ResetPasswordView(View):
    def get(self, request):
        return render(request, 'pages-RecuperarCuenta.html')

    def post(self, request):
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return HttpResponse("El correo electrónico no está registrado.")

        new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
        user.set_password(new_password)
        user.save()

        subject = 'Recuperación de contraseña'
        message = render_to_string('recuperacion_contrasena_email.html', {'new_password': new_password})
        from_email = 'ramgear117@gmail.com'
        recipient_list = [email]

        send_mail(subject, message, from_email, recipient_list, html_message=message)

        return HttpResponse("Se ha enviado una nueva contraseña a su correo electrónico.")
    
    
# clase para exportar excel USUARIOS
class ExportToExcelView(View):
    def get(self, request):
        # Obtén los datos que deseas exportar, por ejemplo, usuarios
        users = User.objects.all()

        # Configura la respuesta HTTP como un archivo Excel descargable
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="usuarios.xlsx"'

        # Crea un libro y una hoja de trabajo en Excel
        workbook = xlsxwriter.Workbook(response)
        worksheet = workbook.add_worksheet()

        # Definir formato personalizado si es necesario
        bold = workbook.add_format({'bold': True})

        # Escribir encabezados en la hoja de trabajo
        worksheet.write(0, 0, 'ID', bold)
        worksheet.write(0, 1, 'Nombre de Usuario', bold)
        worksheet.write(0, 2, 'Correo Electrónico', bold)
        worksheet.write(0, 3, 'Estado', bold)

        # Escribir datos de usuarios en la hoja de trabajo
        row = 1
        for user in users:
            worksheet.write(row, 0, user.id)
            worksheet.write(row, 1, user.username)
            worksheet.write(row, 2, user.email)
            worksheet.write(row, 3, 'Activo' if user.is_active else 'Inactivo')
            row += 1

        # Cierra el libro de trabajo y devuelve la respuesta HTTP
        workbook.close()
        return response