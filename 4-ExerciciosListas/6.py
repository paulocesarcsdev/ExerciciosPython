'''
Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
'''

notas = []
medias  = []
soma = 0
conta_alunos = 1

print('-=-=-=-=-Programa para calcular a media-=-=-=-=-')

for _ in range(3):
    for _ in range(4):
        nota = float(input('Entre com a nota do aluno {} : '.format(conta_alunos)))
        notas.append(nota)
        media = sum(notas) / len(notas)
    medias.append(media)
    if media >= 7.0:
        soma += 1
    conta_alunos += 1
    print('\n')
    notas.clear()
        
print(' [{}] : Número de alunos com nota maior que 7 '.format(soma))