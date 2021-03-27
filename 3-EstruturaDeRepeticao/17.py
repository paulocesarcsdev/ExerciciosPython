'''
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
'''

contador = 2
fatorial = 1

n = 5
if(n <= 1):
    print('1')
else:
    while(contador <= n):
        fatorial = fatorial * contador
        contador += 1
    print(fatorial)