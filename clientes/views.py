from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication 
from rest_framework.permissions import IsAuthenticated 

from clientes.models import Cliente
from clientes.serializers import ClienteSerializer



class ClientesViewSet(viewsets.ModelViewSet):
    '''Exibindo todos os clientes'''
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']
    filterset_fields = ['ativo']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]