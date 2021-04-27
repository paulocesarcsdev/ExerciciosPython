'''
Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
Imprima os três vetores.
'''
numeros = []
par = []
impar = []

for i in range(20):
    numero = int(input('Entre com os números: '))
    numeros.append(numero)
    
    if numero % 2 == 0:
        par.append(numero)
    if numero % 2 != 0:
        impar.append(numero)
        
print('Números par {}'.format(par))
print('Números impar {}'.format(impar))
print('Todos os números {}'.format(numeros))