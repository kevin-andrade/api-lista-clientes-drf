from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=50, blank=False, unique=True)
    cpf = models.CharField(max_length=11, unique=True, blank=False)
    rg = models.CharField(max_length=9, unique=True, blank=False)
    celular = models.CharField(max_length=14, blank=False)
    ativo = models.BooleanField()
    
    def __str__(self):
        return self.nome