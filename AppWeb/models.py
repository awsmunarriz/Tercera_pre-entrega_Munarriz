from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField()
    direccion = models.CharField(max_length=255)
    numero_telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre


class Orden(models.Model):
    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('En Proceso', 'En Proceso'),
        ('Completada', 'Completada'),
        ('Cancelada', 'Cancelada'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_orden = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=20, choices=ESTADO_CHOICES, default='Pendiente')

    def __str__(self):
        return f'Orden {self.id} - {self.cliente.nombre}'

    class Meta():

        verbose_name = 'Orden'
        verbose_name_plural = 'Ordenes'
