from rest_framework import viewsets

from clientes.models import Cliente
from clientes.serializers import ClienteSerializer


class ClientesViewSet(viewsets.ModelViewSet):
    '''Exibindo todos os clientes'''
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer