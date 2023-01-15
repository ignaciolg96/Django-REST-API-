from .models import Medidor, Medicion
from rest_framework import viewsets, permissions
from .serializers import MedidorSerializer, MedicionSerializer,StatSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class MedidorViewSet(viewsets.ModelViewSet):
    queryset = Medidor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MedidorSerializer
    
    @action(detail=True,methods=['get'])
    def estadisticas(self, request, pk=None):
        stats = Medidor.objects.get(id=pk)
        serializer = StatSerializer(stats)
        return Response(serializer.data)
        

        
class MedicionViewSet(viewsets.ModelViewSet):
    queryset = Medicion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MedicionSerializer


    