'''
Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
    Compara duas strings
    String 1: Brasil Hexa 2006
    String 2: Brasil! Hexa 2006!
    Tamanho de "Brasil Hexa 2006": 16 caracteres
    Tamanho de "Brasil! Hexa 2006!": 18 caracteres
    As duas strings são de tamanhos diferentes.
    As duas strings possuem conteúdo diferente.
'''

def tamanho_string(wordOne, wordTwo):
    comprimento1 = len(wordOne)
    comprimento2 = len(wordTwo)
    if wordOne == wordTwo:
        print('A string e igual')
    elif(comprimento1 == comprimento1):
        print('As strings tem o mesmo comprimento: ')
    else:
        print('As string são diferentes')  
    print('A primeira palavra [{}] seu comprimento [{}]a segunda [{}] seu comprimento [{}]'.format(wordOne,comprimento1,wordTwo,comprimento2))


palavra1 = str(input('Entre com a primeira palavra : '))
palavra2 = str(input('Entre com a segunda palavra : '))
tamanho_string(palavra1,palavra2)




