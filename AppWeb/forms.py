from django import forms
from .models import Categoria, Cliente, Producto, Orden


class ClienteFormulario(forms.Form):
    cliente = forms.CharField()
    correo_electronico = forms.EmailField()
    direccion = forms.CharField()
    numero_telefono = forms.CharField()


class CategoriaFormulario(forms.Form):
    categoria = forms.CharField()


class ProductoFormulario(forms.Form):
    nombre = forms.CharField()
    descripcion = forms.CharField(widget=forms.Textarea)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all())
    stock = forms.IntegerField()


class ProductoFormulario(forms.Form):
    nombre = forms.CharField()
    descripcion = forms.CharField(widget=forms.Textarea)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all())
    stock = forms.IntegerField()


class OrdenFormulario(forms.Form):
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all())
    producto = forms.ModelChoiceField(queryset=Producto.objects.all())
    cantidad = forms.IntegerField()
    estado = forms.ChoiceField(choices=Orden.ESTADO_CHOICES)
