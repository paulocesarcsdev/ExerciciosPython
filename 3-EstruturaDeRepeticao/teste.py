gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']

#respostas = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'G', 'H']

respostas = []
alunos = []
soma = 0
notas = []
sair = True

aluno = 1
while(sair != 0):
    print("\n" * 5)
    print("Aluno n°", aluno, ":")

    for i in range(10):
        resposta = input('Entre com a letra das repostas: ')
        respostas.append(resposta)

    for i in range(10):
        if respostas[i] == gabarito[i]:
            soma += 1
        alunos.append(soma)
    aluno += 1
    continuar = input("Outro aluno vai utilizar o sistema? [s/n] : ")
    print(alunos)