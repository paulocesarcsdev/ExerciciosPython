'''
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número
do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto
e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
'''


alunos = []

maior_altura = -1
menor_altura = 999

for i in range(10+1):
    numero_aluno = int(input('Número do aluno: '))
    altura_aluno = float(input('Altura Aluno: '))
    alunos.append({'Numero':numero_aluno,'Altura':altura_aluno})
    
    
    for x in alunos:
        if x['Numero'] > maior_altura:
            NnumeroMaior_altura = x['Numero']
            maior_altura = x['Altura']
        if x['Numero'] < menor_altura:
            menor_altura = x['Numero']
            menor_altura = x['Altura']


print('O menor aluno: ', maior_altura)
print('O maior aluno: ',menor_altura)
