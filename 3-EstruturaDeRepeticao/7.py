'''
Faça um programa que leia 5 números e informe o maior número.
'''

numero = []

contador = 0
while(contador < 5):
    valor = int(input("Entre com números: "))
    numero.append(valor)
    contador += 1
    numero.sort()
print(numero[-1])