'''
Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia.
Um número primo é aquele que é divisível apenas por um e por ele mesmo. 
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
'''


print('Cálculo de número primo')

numero = int(input('Entre com o número: '))
while(numero % 2 == 0):
    print('O número não {} e primo digite novamente'.format(numero))
    numero = int(input('Entre com o número: '))
    
print('O número {} e primo'.format(numero))
