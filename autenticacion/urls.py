from django.urls import path
from . views import *


urlpatterns = [
 
    path('', VRegistro.as_view(), name='Autenticacion'),
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
    path('login/', logear, name='login'),
]

