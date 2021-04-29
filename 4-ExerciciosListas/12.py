'''
Foram anotadas as idades e alturas de 30 alunos.
Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
'''

idades = []
alturas = []
contar_idade = 0

for i in range(3):
    idade = int(input('Entre com a idade: '))
    idades.append(idade)
    
    altura = float(input('Entre com a altura cm : '))
    alturas.append(altura)
    
    altura_media = sum(alturas) / len(alturas)
    
    if idade > 13:
        contar_idade += 1
    
print('Idade {} '.format(idades))
print('Altura: {} '.format(alturas))
print('Alunos {} com menor de 13 anos: '.format(contar_idade))
print('Altura média {} '.format(altura_media))