'''
Jogo de Craps. Faça um programa de implemente um jogo de Craps.
O jogador lança um par de dados, obtendo um valor entre 2 e 12.
Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou.
Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu.
Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto".
Seu objetivo agora é continuar jogando os dados até tirar este número novamente.
Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
''' 

import random

dado = 0

def craps(dado):
    dado = random.randrange(2, 13)
    if dado == 7 or dado == 11:
        print('você um "natural" e ganhou. {} '.format(dado))
    elif dado == 4 or dado == 5 or dado == 8 or dado == 9 or dado == 10:
        print('este é seu "Ponto". {} '.format(dado))
        
        
        ponto = 0
        while ponto != dado:
            entrada = input('Aperte ENTER para fazer a jogada: ')
            if entrada == "":
                ponto = random.randrange(2,13)
                print('O número e {} '.format(ponto))
                if ponto == 7:
                    print('Perdeu!!!, tente novamente')
                    break
    else:
        print('Craps, você perdeu!')
craps(dado)