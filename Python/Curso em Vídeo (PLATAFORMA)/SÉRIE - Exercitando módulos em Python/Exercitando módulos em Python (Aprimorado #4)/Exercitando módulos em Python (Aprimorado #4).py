from utilidadesCeV.dado import dado
from utilidadesCeV.moeda import moeda

p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 80, 35)