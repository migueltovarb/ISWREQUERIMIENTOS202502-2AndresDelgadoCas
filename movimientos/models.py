from django.db import models
from productos.models import Producto

class Movimiento(models.Model):
    TIPO_CHOICES = [
        ('ENTRADA', 'Entrada'),
        ('SALIDA', 'Salida'),
    ]

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    cantidad = models.IntegerField()
    motivo = models.CharField(max_length=200)
    usuario = models.CharField(max_length=100)
    fecha_movimiento = models.DateTimeField(auto_now_add=True)
    referencia = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name_plural = "Movimientos"

    def __str__(self):
        return f"{self.tipo} - {self.producto.nombre} - {self.cantidad}"

    def save(self, *args, **kwargs):
        # Actualizar stock del producto
        if self.tipo == 'ENTRADA':
            self.producto.stock_actual += self.cantidad
        else:  # SALIDA
            self.producto.stock_actual -= self.cantidad
        self.producto.save()
        super().save(*args, **kwargs)