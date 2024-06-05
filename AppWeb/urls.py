from django.urls import path
from AppWeb.views import lista_productos, inicio, productos, categorias
from AppWeb.views import clientes, ordenes, cliente_formulario, categoria_formulario
from AppWeb.views import  producto_formulario, orden_formulario, busqueda_cliente, buscar

urlpatterns = [
    path('lista-productos/', lista_productos),
    path('', inicio, name='Inicio'),
    path('productos/', productos, name='Productos'),
    path('categorias/', categorias, name='Categorias'),
    path('clientes/', clientes, name='Clientes'),
    path('ordenes/', ordenes, name='Ordenes'),
    path('cliente-formulario/', cliente_formulario, name='ClienteFormulario'),
    path('categoria-formulario/', categoria_formulario,
         name='CategoriaFormulario'),
    path('producto-formulario/', producto_formulario, name='ProductoFormulario'),
    path('orden-formulario/', orden_formulario, name='OrdenFormulario'),
    path('busqueda-cliente/', busqueda_cliente, name='BusquedaCliente'),
    path('buscar/', buscar, name='BuscarCliente'),
]
