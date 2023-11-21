from django.http import HttpResponse
import paypalrestsdk
from paypalrestsdk import CreditCard


def payment(request):
    paypalrestsdk.configure({
        "mode": "live",  # Cambia a "live" para producción
        "client_id": "AS2X0MGUy2H4K5yLZMvTicNBjNuJRzbtJaDnB-EUhvlSxdviGhD13p5205HErrDiSSkVrHuOEproxgYE",
        "client_secret": "EM5xQJlLSJQfP_vea7VN88QNUNXOKkh8n21TaDohAq3LvgGFUXP1PUKlCAKJZeLIjlugrPmrYFkPvTEg"
    })
    