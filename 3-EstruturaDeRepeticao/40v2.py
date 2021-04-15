'''
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número
do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto
e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
'''

numero_aluno = int(input('Número do aluno: '))
altura_aluno = float(input('Altura Aluno: '))

menor_altura = altura_aluno
menor_aluno = numero_aluno

maior_altura = altura_aluno
maior_aluno = numero_aluno


for _ in range(9):
    numero_aluno = int(input('Número do aluno: '))
    altura_aluno = float(input('Altura Aluno: '))
    
    if altura_aluno > maior_altura:
        maior_altura = altura_aluno
        maior_aluno = numero_aluno
    elif altura_aluno < menor_altura:
        menor_altura = altura_aluno
        menor_aluno = numero_aluno


print('O menor aluno: ', menor_aluno)
print('A altura do menor aluno: ',menor_altura)
print('O maior aluno: ',maior_aluno)
print('A altura do maior aluno: ', maior_altura)
