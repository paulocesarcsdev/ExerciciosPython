'''
Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. 
A entrada de dados deverá terminar quando for lido um número negativo.
'''

contador = 0
numeros = []

soma_0_25 = 0
soma_26_50 = 0
soma_51_75 = 0
soma_76_100 = 0


numero = int(input('Quantidade de números: '))

while(numero != 0):
    numero = int(input('Quantidade de números: '))
    numeros.append(numero+1)

    if numero > 0 and numero < 25:
        soma_0_25 += 1
    elif numero >= 26 and numero < 50:
        soma_26_50 += 1
    elif numero >= 51 and numero < 75:
        soma_51_75 += 1
    elif numero >= 76 and numero < 100:
        soma_76_100 += 1
    
print('[0-25] ',soma_0_25)
print('[26-50] ',soma_26_50)
print('[51-75] ',soma_51_75)
print('[76-100] ',soma_76_100)