from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from gerencia.api.views import CarroViewSet, EstacionamenoViewSet, VagaEstacionamentoViewSet, ClienteViewSet, TransacaoViewSet

router = DefaultRouter()
router.register("api/cliente", ClienteViewSet, basename="cliente")
router.register("api/carro", CarroViewSet, basename="carro")
router.register("api/estacionamento", EstacionamenoViewSet, basename="estacionamento")
router.register("api/vaga-estacionamento", VagaEstacionamentoViewSet, basename="vaga")
router.register("api/transacao", TransacaoViewSet, basename="transacao")



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    
] + router.urls
