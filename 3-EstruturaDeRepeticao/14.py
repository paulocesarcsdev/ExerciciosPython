'''
Faça um programa que peça 10 números inteiros, calcule e 
mostre a quantidade de números pares e a quantidade de números impares.
'''
lista = []
contador = 0

while(contador <= 10):
    numero = int(input('Entre com dez {} números inteiros :'.format(contador)))
    lista.append(numero)
    for i in range(len(lista)):
        if(i % 2 != 0):
            print(i)
    contador += 1