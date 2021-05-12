'''
Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.
    F
    U
    L
    A
    N
    O
'''
def nome_vertical(nome):
    for palavra in nome:
        print(palavra.upper())


nome = str(input('Entre com seu nome: '))
nome_vertical(nome)