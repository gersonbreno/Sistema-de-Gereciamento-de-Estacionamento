from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.views import APIView
from gerencia.api.serializers import CarroSerializer,Estacionamento, VagaEstacionamento,Carro, Cliente, Transacao, ClienteSerializer, VagaEstacionamentoSerializer, TrasacaoSerializer, EstacionamentoSerializer
from django.shortcuts import get_object_or_404

class CarroViewSet(ModelViewSet):
    serializer_class =  CarroSerializer
    queryset = Carro.objects.all()
    @action(methods=['get'], url_path='search', detail=False)
    def search(self, request):
        nome_desejado = request.query_params.get('modelo', '')
        pizzas = Carro.objects.filter(modelo__icontains = nome_desejado) #Consulta
        serializer = CarroSerializer(pizzas, many=True) #O resultado sendo convertido com serializer
        return Response(
            {"info":"Carro encontrados", "data":serializer.data}, #Enviando o serializer como resposta
            status=status.HTTP_200_OK) #Definido o código HTTP da resposta.

class EstacionamenoViewSet(ModelViewSet):
    serializer_class =  EstacionamentoSerializer
    queryset = Estacionamento.objects.all()
    lookup_field = 'pk'  # Adicione esta linha para indicar que o identificador é 'pk'

    @action(detail=False, methods=['get'])
    def vaga_disponivel(self, request):
        estacionamentos = self.get_queryset()
        vagas_disponiveis = [{'id': estacionamento.id, 'vagas_disponiveis': estacionamento.vaga_disponivel()} for estacionamento in estacionamentos]
        return Response({'estacionamentos': vagas_disponiveis}, status=status.HTTP_200_OK)
    
    
class ClienteViewSet(ModelViewSet):
    serializer_class =  ClienteSerializer
    queryset = Cliente.objects.all()

class VagaEstacionamentoViewSet(ModelViewSet):
    serializer_class =  VagaEstacionamentoSerializer
    queryset = VagaEstacionamento.objects.all()
    

class TransacaoViewSet(ModelViewSet):
    serializer_class =  TrasacaoSerializer
    queryset = Transacao.objects.all()
    @action(detail=True, methods=['get'])
    def calcular_duracao(self, request, pk=None):
        transacao = self.get_object()
        duracao = transacao.calcular_duracao().total_seconds() // 3600  # Duracao em horas
        return Response({'duracao_horas': duracao}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def calcular_valor(self, request, pk=None):
        transacao = self.get_object()
        valor = transacao.calcular_valor()
        return Response({'valor': valor}, status=status.HTTP_200_OK)