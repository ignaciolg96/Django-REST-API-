from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

# Create your models here.

class Medidor(models.Model): 
    llave_id = models.CharField(max_length=32)
    nombre = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.nombre} (id: {self.llave_id})'

class Medicion(models.Model):
    medidor = models.ForeignKey('Medidor', 
        related_name='Medicion', 
        on_delete=models.CASCADE,
        )

    fecha = models.DateTimeField(auto_now_add=True) 
    
    consumo_registrado_kwH = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        validators=[MinValueValidator(Decimal('0'))]
        )
