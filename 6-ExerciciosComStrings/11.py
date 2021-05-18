'''
Jogo de Forca.
Desenvolva um jogo da forca.
O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente.
O jogador poderá errar 6 vezes antes de ser enforcado.

    Digite uma letra: A
    -> Você errou pela 1ª vez. Tente de novo!

    Digite uma letra: O
    A palavra é: _ _ _ _ O

    Digite uma letra: E
    A palavra é: _ E _ _ O

    Digite uma letra: S
    -> Você errou pela 2ª vez. Tente de novo!

'''



palavra = ['a', 'b', 'a', 'c', 'a', 't', 'e']
letras_certas = []


for i in range(0,len(palavra)):
    letras_certas.append('_')
    
acertou = False

while(acertou == False):
    letra = str(input('Entre com a letra '))
    
    for i in range(0, len(palavra)):
        if letra == palavra[i]:
            letras_certas[i] == letra
        print(letras_certas[i])
    acertou = True
    
    for j in range(0, len(letras_certas)):
        if letras_certas[j] == '_':
            acertou = False