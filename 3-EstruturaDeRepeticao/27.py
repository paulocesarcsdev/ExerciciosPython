'''
Faça um programa que calcule o número médio de alunos por turma.
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. 
As turmas não podem ter mais de 40 alunos.
'''

quantidade_turmas =  int(input('Quantidade de turmas: '))

total_alunos = []

for i in range(quantidade_turmas):
    quantidade_alunos = int(input('Entre com a quantidade de alunos da turma {}: '.format(i+1)))

    while(quantidade_alunos > 40):
        print('A quantidade de alunos por turma precisa ser menor que 40: ')
        quantidade_alunos = int(input('Entre com a quantidade de alunos da turma {}: '.format(i+1)))
    i += 1
    total_alunos.append(quantidade_alunos)
    media_turma = sum(total_alunos) // len(total_alunos)
    
print('A média de alunos por turma e {}'.format(media_turma))
