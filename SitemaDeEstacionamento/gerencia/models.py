from django.db import models
from django.utils import timezone

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

class Estacionamento(models.Model):
   
    nome = models.CharField(max_length=100)
    capacidade_total = models.PositiveIntegerField()
    
    def __str__(self):
        return self.nome
    def vaga_disponivel(self):
        vagas_ocupadas = Transacao.objects.filter(vaga__estacionamento=self, saida__isnull=True).count()
        return self.capacidade_total - vagas_ocupadas
class VagaEstacionamento(models.Model):
    estacionamento = models.ForeignKey(Estacionamento, on_delete=models.CASCADE)
    numero_vaga = models.PositiveIntegerField()
    ocupada = models.BooleanField(default=False)

    def __str__(self):
        return f'Vaga {self.numero_vaga} - {self.estacionamento}'

class Carro(models.Model):
    placa = models.CharField(max_length=20, unique=True)
    modelo = models.CharField(max_length=50)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.modelo} - {self.placa}'

class Transacao(models.Model):
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    vaga = models.ForeignKey(VagaEstacionamento, on_delete=models.CASCADE)
    entrada = models.DateTimeField(auto_now_add = True)
    saida = models.DateTimeField(null=True, blank=True)

    def calcular_duracao(self):
        if self.saida is not None:
            return self.saida - self.entrada
        else:
            return timezone.now() - self.entrada

    def calcular_valor(self):
        # Lógica para calcular o valor com base na duracao, python manage.py makemigrationstarifas, etc.
        # Este é um exemplo simples e pode ser ajustado conforme necessário.
        duracao = self.calcular_duracao().total_seconds() // 3600  # Duracao em horas
        tarifa_hora = 5  # Valor por hora
        return duracao * tarifa_hora

    def __str__(self):
        return f'Transação - {self.carro} - {self.vaga} - Entrada: {self.entrada} - Saída: {self.saida}'
 