'''
Faça um programa com uma função chamada somaImposto.
A função possui dois parâmetros formais:
taxaImposto, que é a quantia de imposto sobre vendas expressa em
porcentagem e custo, que é o custo de um item antes do imposto.
A função “altera” o valor de custo para incluir o imposto sobre vendas.
'''


def somaImposto(taxaImposto, custo):
    custo += (taxaImposto / 100)
    return custo 

custo_valor = float(input('Entre com o valor do produto: R$ '))
taxa_imposto = float(input('Entre com o valor da taxa de imposto: R$ '))
total = somaImposto(taxa_imposto,custo_valor)
print(total)