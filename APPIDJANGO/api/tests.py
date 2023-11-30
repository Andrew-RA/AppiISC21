from django.test import TestCase

# Create your tests here.
import pytest
from django.contrib.auth.models import User
from api.models import Cliente, Atraccion, Cotizacion, Venta, Evento, UserProfile

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
    



@pytest.mark.django_db
def test_atraccion_model():
    # Creamos una atracción de prueba
    atraccion = Atraccion.objects.create(
        nombre='Atracción de prueba',
        descripcion='Descripción de prueba',
        precio=10.50
    )

    # Verificamos que la representación de la atracción sea el nombre de la atracción
    assert str(atraccion) == 'Atracción de prueba'

    # Verificamos que los campos de la atracción sean correctos
    assert atraccion.nombre == 'Atracción de prueba'
    assert atraccion.descripcion == 'Descripción de prueba'
    assert atraccion.precio == 10.50




@pytest.mark.django_db
def test_evento_model():
    # Creamos una atracción de prueba
    atraccion = Atraccion.objects.create(
        nombre='Atracción de prueba',
        descripcion='Descripción de prueba',
        precio=10.50
    )

    # Creamos un evento de prueba
    evento = Evento.objects.create(
        nombre='Evento de prueba',
        fecha_inicio='2023-11-29T12:00:00Z',
        fecha_fin='2023-11-29T18:00:00Z'
    )


@pytest.mark.django_db
def test_venta_model():
    # Creamos un usuario de prueba
    user = User.objects.create(username='testuser')

    # Creamos un cliente de prueba
    cliente = Cliente.objects.create(
        user=user,
        telefono='123456789',
        direccion='Calle de prueba, Ciudad de prueba'
    )

    # Creamos una atracción de prueba
    atraccion = Atraccion.objects.create(
        nombre='Atracción de prueba',
        descripcion='Descripción de prueba',
        precio=10.50
    )

    # Creamos una cotización de prueba
    cotizacion = Cotizacion.objects.create(
        cliente=cliente,
        fecha_creacion='2023-11-29T12:00:00Z',
        fecha_modificacion='2023-11-29T12:00:00Z'
    )

    # Asociamos la atracción a la cotización
    cotizacion.atracciones.add(atraccion)

    # Creamos una venta de prueba
    venta = Venta.objects.create(
        cotizacion=cotizacion
    )

    # Verificamos que la representación de la venta sea correcta
    assert str(venta) == f'Venta de testuser - {venta.fecha_venta}'

    # Verificamos que los campos de la venta sean correctos
    assert venta.cotizacion == cotizacion
    assert venta.cotizacion.cliente == cliente


@pytest.mark.django_db
def test_user_profile_model():
    # Creamos un usuario de prueba
    user = User.objects.create(username='testuser')

    # Creamos un UserProfile de prueba
    user_profile = UserProfile.objects.create(
        user=user
    )

    # Verificamos que los campos del UserProfile sean correctos
    assert user_profile.user == user