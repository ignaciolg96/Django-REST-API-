from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.db.models import Avg, Max, Min, Sum
from django.utils import timezone


# Create your models here.

class Medidor(models.Model): 
    llave_id = models.CharField(max_length=32)
    nombre = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.nombre} (id: {self.llave_id})'

    @property
    def estadisticas(self):
        consumoMaximo = Medicion.objects.all().filter(medidor=self.id).aggregate(Max('consumo_registrado_kwH'))
        consumoMinimo = Medicion.objects.all().filter(medidor=self.id).aggregate(Min('consumo_registrado_kwH'))
        consumoTotal = Medicion.objects.all().filter(medidor=self.id).aggregate(Sum('consumo_registrado_kwH'))
        consumoPromedio = Medicion.objects.all().filter(medidor=self.id).aggregate(Avg('consumo_registrado_kwH'))
        estadisticas = {
            'Consumo Maximo':consumoMaximo.get('consumo_registrado_kwH__max'),
            'Consumo Minimo':consumoMinimo.get('consumo_registrado_kwH__min'),
            'Consumo Total':consumoTotal.get('consumo_registrado_kwH__sum'),
            'Consumo Promedio':consumoPromedio.get('consumo_registrado_kwH__avg')
        }
        return estadisticas

class Medicion(models.Model):
    medidor = models.ForeignKey(
        'Medidor', 
        related_name='mediciones', 
        on_delete=models.DO_NOTHING,
        )

    fecha = models.DateTimeField(auto_now_add=True) 
    
    consumo_registrado_kwH = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        validators=[MinValueValidator(Decimal('0'))]
        )

    def __str__(self):
        return f'Consumo: {self.consumo_registrado_kwH} kwH)'

