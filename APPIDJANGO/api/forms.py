from django import forms

class ExportarDatosForm(forms.Form):
    seleccionar_campos = forms.MultipleChoiceField(
        choices=(
            ('nombre', 'Nombre'),
            ('edad', 'Edad'),
            ('correo', 'Correo Electrónico'),
        ),
        widget=forms.CheckboxSelectMultiple
    )
    