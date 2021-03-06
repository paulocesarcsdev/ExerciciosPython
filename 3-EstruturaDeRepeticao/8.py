'''
Faça um programa que leia 5 números e informe a soma e a média dos números.
'''
contador = 0
soma = 0
while(contador < 5):
    numero = int(input("Entre com 5 números: "))
    soma += numero
    media = (soma / 5)
    contador += 1
print('Media {}'.format(media))
    