# Generated by Django 5.0.2 on 2024-02-13 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gerencia', '0003_estacionamento_transacoes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estacionamento',
            name='transacoes',
        ),
    ]
