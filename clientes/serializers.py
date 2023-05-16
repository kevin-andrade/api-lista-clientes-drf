from rest_framework import serializers

from clientes.models import Cliente
from clientes.validators import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    '''Validando campos'''
    def validate(self, data):
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome': 'O campo não pode conter números.'})
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': 'O número de CPF é inválido'})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg': 'O rg não contém 9 dígitos'})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular': 'O número de celular deve seguir esse modelo: 85 91234-1234. (Respeite os espaços e traço)'})
        return data