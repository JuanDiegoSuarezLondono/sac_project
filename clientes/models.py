from django.db import models

class TipoDocumento(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    numero_documento = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    descripcion = models.TextField(blank=True)