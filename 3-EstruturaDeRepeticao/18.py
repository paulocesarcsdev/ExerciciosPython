'''
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
'''

numeros = int(input('Entre com a quantidade de números: '))
numeros_lista = []
contador = 0
num = 0

while(contador <= numeros):
    num = int(input('Entre com os números: '))
    numeros_lista.append(num)
    
    numeros_lista.sort()
    
    menor = min(numeros_lista)
    maior = max(numeros_lista)
    
    soma_maiorMenor = menor + maior
    
    contador += 1
print('valores na lista', numeros_lista)
print('menor valor = ', menor)
print('maior valor = ', maior)
print('soma dos valores =', soma_maiorMenor)