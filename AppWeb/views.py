from django.http import HttpResponse
from django.shortcuts import render
from .models import Producto

def lista_productos(req):

  lista = Producto.objects.all()

  return render(req, "lista_productos.html", {"lista_productos": lista})
