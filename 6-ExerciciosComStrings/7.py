'''
Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

    a. quantos espaços em branco existem na frase.
    b. quantas vezes aparecem as vogais a, e, i, o, u.
'''

palavra = str(input('Entre com a frase/palavra: '))

print(palavra)
contador = 0

vogais = 'aieou'
espaco = ' '
quantidade = palavra.count(vogais)

for i in vogais:
    if i in palavra:
        if i in vogais:
            contador += 1
            
contar_espaco = 0
for i in espaco:
    if i in palavra:
        if i in espaco:
            contar_espaco += 1
            
print('Total de Vogais {} quantidade de espaços {}'.format(contador, contar_espaco))