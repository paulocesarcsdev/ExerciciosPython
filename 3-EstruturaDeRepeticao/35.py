'''
QUANDO TIVER TEMPO REFAZER
Encontrar números primos é uma tarefa difícil. 
Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.
'''

lista = []
numero = int(input('Informe um valor: '))
contador = 0
for i in range(1,numero+1):
    if(i % 2 != 0):
        lista.append(i)
        #print(i, end=' ')
print(lista)
    
    