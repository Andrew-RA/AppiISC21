from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse

class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated:
            if 'last_activity' in request.session:
                last_activity = request.session['last_activity']
                idle_duration = (request.session.modified or request.session.accessed) - last_activity
                if idle_duration > settings.SESSION_COOKIE_AGE: 
                    del request.session['last_activity']
                    return redirect(reverse('login'))  # Ajusta 'login' con el nombre de tu vista de inicio de sesión
            request.session['last_activity'] = response.cookies['sessionid'].coded_value
        return response

