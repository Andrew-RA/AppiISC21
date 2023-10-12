
from django.urls import path
from api.views import Login,Home,RegistraUsuario,RegistroUser, ResetPasswordView,  UserListView, ExportToExcelView


urlpatterns = [
    
    # path('admin/', admin.site.urls),
    path('',Login.as_view(),name='Login'),
    path('RegistraUsuario',RegistraUsuario.as_view(),name='RegistraUsuario'),   
    path('Home',Home.as_view(),name='Home'),
    path('Login',Login.as_view(),name='Login'),
    path('RegistroUser/', RegistroUser.as_view(), name='RegistroUser'),
    path('reset_password/', ResetPasswordView.as_view(), name='reset_password'),
    path('user-list/', UserListView.as_view(), name='user_list'),
    path('export_to_excel/', ExportToExcelView.as_view(), name='export_to_excel'),
]

