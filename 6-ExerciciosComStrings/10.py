'''
Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.
'''
def numeroExteno(numero):
    if(numero == 1):
            print('Um')
    elif(numero == 2):
        print('Dois')
    elif(numero == 3):
        print('Três')
    elif(numero == 4):
        print('Quatro')
    elif(numero == 5):
        print('Cinco')
    else:
        print('Valor não se encontra no intervalo')


numero = int(input('Entre com um número de 1 a 5: '))

numeroExteno(numero)

