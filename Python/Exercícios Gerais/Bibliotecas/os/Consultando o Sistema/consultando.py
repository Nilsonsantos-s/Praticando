"""
Consultando o Sistema
"""
import os

sistema = os.environ
print('-'*30)
print('INFORMAÇÕES DO SISTEMA')
print('-'*30)
print('Nome do Computador:', sistema['COMPUTERNAME'])
print('Nome do Usuário:', sistema['USERNAME'])
print('Pasta raiz do sistema:', sistema['SYSTEMROOT'])
print('Arquitetura do Processador:', sistema['PROCESSOR_ARCHITECTURE'])
print('Processador:', sistema['PROCESSOR_IDENTIFIER'])
