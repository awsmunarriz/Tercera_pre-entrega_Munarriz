from django.urls import path
from AppWeb.views import lista_productos, inicio, productos, categorias, clientes, ordenes


urlpatterns = [
    path('lista-productos/', lista_productos),
    path('', inicio, name='Inicio'),
    path('productos/', productos, name='Productos'),
    path('categorias/', categorias, name='Categorias'),
    path('clientes/', clientes, name='Clientes'),
    path('ordenes/', ordenes, name='Ordenes'),
]
