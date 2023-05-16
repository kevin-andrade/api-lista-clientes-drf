import re
from validate_docbr import CPF


'''Verifica se contém numero no nome'''
def nome_valido(nome):
    return nome.isalpha()

'''Verifica cpf'''
def cpf_valido(numero_cpf):
   cpf = CPF()
   cpf.mask = numero_cpf
   return cpf.validate(numero_cpf)

def rg_valido(numero_rg):
    return len(numero_rg) == 9

def celular_valido(numero_celular):
    '''celular válido = (85) 91234-1234'''
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, numero_celular)
    return resposta
