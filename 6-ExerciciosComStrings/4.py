'''
Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

    F
    FU
    FUL
    FULA
    FULAN
    FULANO

'''
def nome_vertical(nome):
    for palavra in range(len(nome)+1):
        print(nome[:palavra])


nome = str(input('Entre com seu nome: ')).upper()
nome_vertical(nome)