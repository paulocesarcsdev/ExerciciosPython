'''
def nome_vertical(nome):
    for palavra in range(len(nome)+1):
        print(nome[:palavra])

nome = str(input('Entre com seu nome: ')).upper()
nome_vertical(nome)

'''

nome = str(input('Entre com seu nome: ')).upper()
print(nome[:nome])