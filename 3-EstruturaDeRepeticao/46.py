'''
Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões,
o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o
gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa).
Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. 
Após todos os alunos terem respondido informar:

    a) Maior e Menor Acerto;
    b) Total de Alunos que utilizaram o sistema;
    c) A Média das Notas da Turma.

Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A

Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.

'''
#gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']

gabarito = ['A', 'B', 'C', 'D', 'E']

#respostas = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'G', 'H']

respostas = []
alunos = []
soma = 0
notas = []
sair = True

aluno = 1
while sair != 'n':
    print("\n" * 3)
    print("Aluno n°", aluno, ":")

    for i in range(3):
        resposta = input('Entre com a letra das repostas: ')
        respostas.append(resposta)

    for i in range(3):
        if respostas[i] == gabarito[i]:
            soma += 1
        alunos.append(soma)
    aluno += 1
    sair = input("Outro aluno vai utilizar o sistema? [s/n] : ")
    
print('Quantidade de alunos', aluno)
print('Maior nota', max(alunos))
print('Menor nota', min(alunos))
print('Média das notas', sum(alunos) / len(alunos))