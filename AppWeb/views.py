from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *


def lista_productos(req):

    lista = Producto.objects.all()

    return render(req, "lista_productos.html", {"lista_productos": lista})


def inicio(req):

    return render(req, "inicio.html", {})


def productos(req):

    return render(req, "productos.html", {})


def categorias(req):

    return render(req, "categorias.html", {})


def clientes(req):

    return render(req, "clientes.html", {})


def ordenes(req):

    return render(req, "ordenes.html", {})


def cliente_formulario(req):

    if req.method == 'POST':
        miFormulario = ClienteFormulario(req.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            nuevo_cliente = Cliente(nombre=data['cliente'], correo_electronico=data['correo_electronico'],
                                    direccion=data['direccion'], numero_telefono=data['numero_telefono'])
            nuevo_cliente.save()
            return render(req, "inicio.html", {"message": "Cliente creado con éxito"})
        else:
            return render(req, "inicio.html", {"message": "Datos inválidos"})
    else:
        miFormulario = ClienteFormulario()
        return render(req, "cliente_formulario.html", {"miFormulario": miFormulario})


def categoria_formulario(req):

    if req.method == 'POST':
        miFormulario = CategoriaFormulario(req.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            nueva_categoria = Categoria(nombre=data['categoria'])
            nueva_categoria.save()
            return render(req, "inicio.html", {"message": "Categoria creada con éxito"})
        else:
            return render(req, "inicio.html", {"message": "Datos inválidos"})
    else:
        miFormulario = CategoriaFormulario()
        return render(req, "categoria_formulario.html", {"miFormulario": miFormulario})


def producto_formulario(req):

    if req.method == 'POST':
        miFormulario = ProductoFormulario(req.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            nuevo_producto = Producto(
                nombre=data['nombre'],
                descripcion=data['descripcion'],
                precio=data['precio'],
                categoria=data['categoria'],
                stock=data['stock']
            )
            nuevo_producto.save()
            return render(req, "inicio.html", {"message": "Producto creado con éxito"})
        else:
            return render(req, "inicio.html", {"message": "Datos inválidos"})
    else:
        miFormulario = ProductoFormulario()
        return render(req, "producto_formulario.html", {"miFormulario": miFormulario})


def orden_formulario(req):

    if req.method == 'POST':
        miFormulario = OrdenFormulario(req.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            nueva_orden = Orden(
                cliente=data['cliente'],
                producto=data['producto'],
                cantidad=data['cantidad'],
                estado=data['estado']
            )
            nueva_orden.save()
            return render(req, "inicio.html", {"message": "Orden creada con éxito"})
        else:
            return render(req, "inicio.html", {"message": "Datos inválidos"})
    else:
        miFormulario = OrdenFormulario()
        return render(req, "orden_formulario.html", {"miFormulario": miFormulario})


def busqueda_cliente(req):

    return render(req, "busqueda_cliente.html", {})

def buscar(req):

  if req.GET["numero_telefono"]:

    numero_telefono = req.GET["numero_telefono"]

    clientes = Cliente.objects.filter(numero_telefono__icontains=numero_telefono)

    return render(req, "resultadoBusqueda.html", {"clientes": clientes, "numero_telefono": numero_telefono})

  else:
      
      return render(req, "inicio.html", {"message": "No envias el dato del numero_telefono"})