'''
Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

    a. quantos espaços em branco existem na frase.
    b. quantas vezes aparecem as vogais a, e, i, o, u.
'''


def contador_vogaisEspacos(palavra):
    vogais = 'aieou'
    espaco = ' '
    contador_vogais = 0
    for i in palavra:
        if i in vogais:
            contador_vogais += 1
            
    contador_espaco = 0
    for i in palavra:
        if i in espaco:
            contador_espaco += 1
            
    print('Total de Vogais {} , o total des espaços {} '.format(contador_vogais,contador_espaco))
    


palavra = str(input('Entre com a frase/palavra: '))
print()
contador_vogaisEspacos(palavra)

