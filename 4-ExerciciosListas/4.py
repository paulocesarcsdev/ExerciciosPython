'''
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas.
Imprima as consoantes.
'''
vogais = ['a', 'e', 'i', 'o', 'u']
caracteres = []
consoantes = 0
aux = []

contador = 1
contador_caracteres = 0
print('*********Entre com dez caracteres*********')
for i in range(5):
    caracter = input(str('{} : '.format(contador)))
    caracteres.append(caracter)
    if caracter in vogais:
        contador_caracteres += 1
    if caracter not in  vogais:
        aux.append(caracter)
    contador += 1
    consoantes = (len(caracteres)) - contador_caracteres
    

print('Total de consoantes {} '.format(consoantes))
print('As consoantes foram {} '.format(aux))
