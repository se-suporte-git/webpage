from django.urls import path
from esg.views import lista_empresas,login

urlpatterns = [
    path('empresas/', lista_empresas, name='lista_empresas'),
    path('login/', login, name='login'),
]
