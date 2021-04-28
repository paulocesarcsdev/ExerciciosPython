'''
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
'''

numeros = []
soma = 0
multiplicacao = 1
conta_valor = 1

for i in range(5):
    numero = int(input('Entre com 5 valores: {} '.format(conta_valor)))
    numeros.append(numero)
    soma += numero
    multiplicacao *= numero
    conta_valor += 1
    
print(numeros)
print('O valor da soma [{}] '.format(soma))
print('O valor da multiplicação [{}] '.format(multiplicacao))
print('Os números digitados foram {} '.format(numeros))