from django.test import TestCase

# Create your tests here.
import pytest
from django.contrib.auth.models import User
from api.models import Cliente

@pytest.mark.django_db
def test_cliente_model():
    # Creamos un usuario de prueba
    user = User.objects.create(username='testuser')

    # Creamos un cliente de prueba
    cliente = Cliente.objects.create(
        user=user,
        telefono='123456789',
        direccion='Calle de prueba, Ciudad de prueba'
    )

    # Verificamos que la representación del cliente sea el nombre de usuario del usuario asociado
    assert str(cliente) == 'testuser'

    # Verificamos que los campos del cliente sean correctos
    assert cliente.user == user
    assert cliente.telefono == '123456789'
    assert cliente.direccion == 'Calle de prueba, Ciudad de prueba'