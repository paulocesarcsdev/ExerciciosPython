'''
Palíndromo.
Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa.
Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados.
A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados.
Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.
'''

def palindromo(palavra):
    palavra_inversa = palavra[::-1]

    if palavra_inversa == palavra:
        print('A palavra {} Palíndromo. sua inversa e {} '.format(palavra, palavra_inversa))
    else:
        print('A palavra {} não e um Palíndromo, sua inversa e {} '.format(palavra,palavra_inversa))
        

palavra = str(input('Entre com a palavra: ')).upper()
print('')
palindromo(palavra)


