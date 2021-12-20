from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Fornecedor, Funcionario, Veiculo, Cliente
from sistema.models import LANGUAGE_CHOICES, STYLE_CHOICES



class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'rg', 'cnh', 'email', 'senha']

class FornecedorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fornecedor
        fields = ['nome', 'cnpj', 'telefone', 'email', 'senha']

class FuncionarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Funcionario
        fields = ['nome', 'cpf', 'rg', 'cnh', 'email', 'senha']

class VeiculoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Veiculo
        fields = ['classificacao', 'placa', 'cor', 'chassi', 'foto', 'gps',
         'cadeiras', 'tracao', 'ultimadatadisponivel', 'idade']