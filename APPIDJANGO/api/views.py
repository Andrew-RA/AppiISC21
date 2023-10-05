from django.shortcuts import render
from rest_framework.views import APIView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from rest_framework.views import APIView

from django import forms
from django.shortcuts import render
from .models import Persona
from .forms import ExportarDatosForm
from openpyxl import Workbook
from django.http import HttpResponse


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
    
    
    
    
# PRUEBA EXCEL

class ExportarDatosForm(forms.Form):
    seleccionar_campos = forms.MultipleChoiceField(
        choices=(
            ('nombre', 'Nombre'),
            ('edad', 'Edad'),
            ('correo', 'Correo Electrónico'),
        ),
        widget=forms.CheckboxSelectMultiple
    )


def exportar_a_excel(request):
    if request.method == 'POST':
        form = ExportarDatosForm(request.POST)
        if form.is_valid():
            # Obtener los campos seleccionados por el usuario
            campos_seleccionados = form.cleaned_data['seleccionar_campos']

            # Consultar la base de datos para obtener los datos de las personas
            personas = Persona.objects.all()

            # Crear un libro de Excel y una hoja de cálculo
            wb = Workbook()
            ws = wb.active

            # Agregar encabezados de columna al archivo Excel
            ws.append(campos_seleccionados)

            # Agregar datos al archivo Excel
            for persona in personas:
                datos_persona = [getattr(persona, campo) for campo in campos_seleccionados]
                ws.append(datos_persona)

            # Crear una respuesta HTTP con el archivo Excel adjunto
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=exportacion_datos.xlsx'
            wb.save(response)

            return response
    else:
        form = ExportarDatosForm()

        return render(request, 'datos.html', {'form': form})

