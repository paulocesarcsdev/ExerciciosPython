'''
Foram anotadas as idades e alturas de 30 alunos.
Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
'''

idades = []
alturas = []
contar_idade = 0

for i in range(30):
    idade = int(input('Entre com a idade: '))
    idades.append(idade)
    
    altura = float(input('Entre com a altura cm : '))
    alturas.append(altura)
    
    altura_media = sum(alturas) / len(alturas)
    total = 0
    
for i in range(30):
    if idades[i] > 13 and alturas[i] < altura_media:
        total += 1
    
    
#print('Idade {} '.format(idades))
#print('Altura: {} '.format(alturas))
#print('Alunos {} com menor de 13 anos: '.format(contar_idade))
#print('Altura média {} '.format(altura_media))
print('Total de alunos com mais de 13 anos e altura inferio a media de altura: {} '.format(total))