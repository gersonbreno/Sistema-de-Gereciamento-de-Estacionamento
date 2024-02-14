from rest_framework import serializers
from gerencia.models import Cliente, Estacionamento, VagaEstacionamento, Carro, Transacao

class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = "__all__"


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"
class EstacionamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estacionamento
        fields = "__all__"

class VagaEstacionamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VagaEstacionamento
        fields = "__all__"

class TrasacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacao
        fields = "__all__"