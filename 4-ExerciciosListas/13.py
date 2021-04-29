'''
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
'''


temperaturas = []

conta_temperatura = 1
for i in range(12):
    temperatura = float(input('Entre com a temperatura do mês {} : '.format(conta_temperatura)))
    temperaturas.append(temperatura)
    
    conta_temperatura += 1
    
print(temperaturas)