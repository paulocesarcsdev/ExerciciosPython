'''
Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 
Dica: utilize uma função de arredondamento.
'''

numero = float(input('Entre com o numero: '))
aux = (round(numero))
if(aux != numero):
    print('Decimal')
else:
    print('Ineiro')
