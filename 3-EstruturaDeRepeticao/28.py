'''
Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. 
O usuário deverá informar a quantidade de CDs e o valor para em cada um.
'''

quantidade_cd = int(input('Por favor informe a quantidade de CD´s: ' ))

valor_cd = []

print('Entre com os preços de cada CD: ')

for i in range(quantidade_cd):
    precos = int(input('Valor do CD {} R$ '.format(i+1)))
    valor_cd.append(precos)
    
    i += 1
    valor_medio = sum(valor_cd) / len(valor_cd)

print('O valor médio gasto por CD R$ {} '.format(valor_medio) )