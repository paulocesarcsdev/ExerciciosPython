'''
Nome ao contrário em maiúsculas.
Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre
o nome do usuário de trás para frente utilizando somente letras maiúsculas.
Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.
'''

def contraio_minusculo(nome):
    inverso = nome[::-1].lower()
    print(inverso)

print('Entre com o nome completo em maisuclo: ')
nome = str(input('Entre com o nome: '))
contraio_minusculo(nome)

