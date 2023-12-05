
from django.urls import path
from api.views import Login,Home,RegistraUsuario,RegistroUser, ResetPasswordView,  UserListView, ExportToExcelView, PaypalCheckOut, powerbi, CalendarView, RegistroUser


urlpatterns = [
    
    # path('admin/', admin.site.urls),
    path('',Login.as_view(),name='Login'),
    path('RegistraUsuario',RegistraUsuario.as_view(),name='RegistraUsuario'),   
    path('Home',Home.as_view(),name='Home'),
    path('Login',Login.as_view(),name='Login'),
    path('correcto/', RegistroUser.as_view(), name='correcto'),
    path('reset_password/', ResetPasswordView.as_view(), name='reset_password'),
    path('user-list/', UserListView.as_view(), name='user_list'),
    path('export_to_excel/', ExportToExcelView.as_view(), name='export_to_excel'),
    path('payment/',PaypalCheckOut.as_view(), name='payment'),
    path('powerbi/',powerbi.as_view(), name='powerbi'),
    path('calendario/', CalendarView.as_view(), name='calendario'),
    
    
 
    
]

