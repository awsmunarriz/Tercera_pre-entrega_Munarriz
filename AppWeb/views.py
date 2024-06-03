from django.http import HttpResponse
from django.shortcuts import render
from .models import Producto


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
