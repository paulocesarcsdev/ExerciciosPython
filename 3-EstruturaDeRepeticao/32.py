'''
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:

Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120

'''

numero = int(input('Entre o valor: '))

contador = numero
fatorial = 1

print('Calculando {}! = '.format(numero), end='')

while contador > 0:
    print('{}'.format(contador), end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador  -=  1
print('{}'.format(fatorial))