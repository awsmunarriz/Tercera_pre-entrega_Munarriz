from django.urls import path
from AppWeb.views import lista_productos, inicio, productos, categorias, clientes, ordenes


urlpatterns = [
    path('lista-productos/', lista_productos),
    path('', inicio),
    path('productos/', productos),
    path('categorias/', categorias),
    path('clientes/', clientes),
    path('ordenes/', ordenes),
]
