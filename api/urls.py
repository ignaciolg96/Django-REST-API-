from django.urls import path, include
from rest_framework import routers
from .api import MedidorViewSet, MedicionViewSet


# Routers para determinar mas facil la conf URL
router = routers.DefaultRouter()
router.register('api/medidores', MedidorViewSet)
router.register('api/mediciones', MedicionViewSet)

# Routing URL automatico
urlpatterns = router.urls