'''
Nome na vertical em escada invertida.
Altere o programa anterior de modo que a escada seja invertida.

    FULANO
    FULAN
    FULA
    FUL
    FU
    F
'''

def nome_vertical(nome):
    for palavra in range(len(nome)+1):
        print(nome[palavra:])
        


nome = str(input('Entre com seu nome: ')).upper()
nome_vertical(nome)