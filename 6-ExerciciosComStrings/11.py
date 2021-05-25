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

from random import choice

alfabeto = list("abdcefghijklmnopqrstuvwxyz")
tentativas = []
vocabulario = ["esquistossomose", "naftalina", 
               "ribonucleico", "idiossincratico", 
               "fagocitose", "quinquagesimo"]
palavra = choice(vocabulario)
chances = 6


    
while True:
    #print(tentativas)
    print('Chances :', chances)
    
    for letra in palavra:
        if letra in tentativas:
            print(letra, end = ' ')
        else:
            print('_', end= ' ')
            
    palpite = input("\nEntre com seu palpite ou 'SAIR' oara sair do programa: ").lower()
    if palpite == 'sair':
        break
    elif palpite not in alfabeto or palpite == '':
        print("Iss não e uma letra")
        continue
    elif palpite in tentativas:
        print('Letra repetida tente novamente')
        continue
    tentativas.append(palpite)
    if palpite in palavra:
        print('Correto')
    else:
        print('Erro tente novamente')
        chances -= 1
    if chances == 0:
        print('Todas tentativas esgostadas fim de jogo: ')
        break
    elif set(palavra).issubset(set(tentativas)):
        print('Parabéns acertou: ')
        break