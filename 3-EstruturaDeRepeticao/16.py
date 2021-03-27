'''
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
Faça um programa que gere a série até que o valor seja maior que 500.
'''

n = int(input('Entre com o valor: '))

ultimo = 1
penultimo = 1
termo = 0

while termo < 500:
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    if termo < 500:
        print(termo, end=' ')
        print('\n')
    else:
        print('O próximo valor será maior que 500')
 
