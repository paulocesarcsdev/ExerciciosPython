'''
Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
'''

numeros = []
soma = 0
for i in range(10):
    numero = int(input('Entre com os números: '))
    numeros.append(numero)
    soma = soma + numero ** 2

print(soma)