from django.urls import path
from AppWeb.views import inicio, lista_productos, lista_categorias 
from AppWeb.views import lista_clientes, lista_ordenes
from AppWeb.views import cliente_formulario, categoria_formulario
from AppWeb.views import  producto_formulario, orden_formulario, busqueda_cliente, buscar

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('lista-productos/', lista_productos, name='ListaProductos'),
    path('lista-categorias/', lista_categorias, name='ListaCategorias'),
    path('lista-clientes/', lista_clientes, name='ListaClientes'),
    path('lista-ordenes/', lista_ordenes, name='ListaOrdenes'),
    path('cliente-formulario/', cliente_formulario, name='ClienteFormulario'),
    path('categoria-formulario/', categoria_formulario,
         name='CategoriaFormulario'),
    path('producto-formulario/', producto_formulario, name='ProductoFormulario'),
    path('orden-formulario/', orden_formulario, name='OrdenFormulario'),
    path('busqueda-cliente/', busqueda_cliente, name='BusquedaCliente'),
    path('buscar/', buscar, name='BuscarCliente'),
]
