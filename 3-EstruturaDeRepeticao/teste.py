'''
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
'''

contador = 2
fatorial = 1

#aux = []

n = 5
fat = 1
i = 2
while i <= n:
        fat = fat*i
        i += 1
        print(fat)