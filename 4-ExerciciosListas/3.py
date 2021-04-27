'''
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
'''
notas = []
contador =1
soma_notas = 0

print('-=-=-=-=-=Por favor entre com 4 notas-=-=-=-=-=')
for i in range(4):
    notas.append(float(input('Nota {}: '.format(contador))))
    soma_notas += notas[i]
    contador += 1

print('Notas: {} '.format(notas))
print('Média das notas: {} '.format(soma_notas / len(notas)))
