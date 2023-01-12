from rest_framework import serializers
from .models import Medicion, Medidor

class MedicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicion
        fields = ('id', 'medidor', 'fecha', 'consumo_registrado_kwH')
        #read_only_fields = ('id', 'medidor', 'fecha', 'consumo_registrado_kwH')

class MedidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medidor
        fields = ('id', 'llave_id', 'nombre')
        #read_only_fields = ('id', 'llave_id', 'nombre')