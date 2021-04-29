'''
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
'''
teste = []
meses = ['Janeiro', 'Feveriro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
         'Agosto', 'Setembro', 'Outrubo', 'Novembro', 'Dezembro']
temperaturas = []
contar_temperaturas = 0

conta_mes = 1
for i in range(12):
    temperatura = float(input('Entre com a temperatura do mês {} : '.format(conta_mes)))
    temperaturas.append(temperatura)
    
    
    media_anual = sum(temperaturas) / len(temperaturas)
    conta_mes += 1

for i in range(12):
    if temperaturas[i] > media_anual and meses[i]:
        teste.append(i+1)
        print(meses[i])
