'''
Faça um programa que calcule o mostre a média aritmética de N notas.
'''

numero_notas = int(input("Entre o total de notas : "))
total = 0
for i in range(numero_notas):
    notas = int(input('Notas: '))
    total += notas
    media = total / numero_notas
print(media)