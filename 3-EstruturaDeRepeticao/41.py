'''
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:

    a) Código da cidade;
    b) Número de veículos de passeio (em 1999);
    c) Número de acidentes de trânsito com vítimas (em 1999). 
    Deseja-se saber:
    d) Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
    e) Qual a média de veículos nas cinco cidades juntas;
    f) Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

'''

codigos_cidades = []
numeros_veiculos = []
numeros_acidentes = []
menor_que200 = []

for _ in range(5):
    codigo_cidade = int(input('Entre com o código da cidade: '))
    codigos_cidades.append(codigo_cidade)
    
    numero_veiculo = int(input('Número de veículos de passeio (em 1999): ' ))
    numeros_veiculos.append(numero_veiculo)
    
    numero_acidente = int(input('Número de acidentes de trânsito com vítimas (em 1999): '))
    numeros_acidentes.append(numero_acidente)
    
    if(numero_veiculo > 2000):
        menor_que200.append(numero_veiculo)
        numeros_acidentes.append(numero_acidente)
    
maior_indice_acidentes = numeros_acidentes.index(max(numeros_acidentes))
menor_indice_acidentes = numeros_acidentes.index(min(numeros_acidentes))
media_veiculos = sum(numeros_veiculos) / len(numeros_veiculos)
media_acidentes200 = sum(numeros_acidentes) / len(numeros_acidentes)

    
print('A maior indicie de acidentes pertence a cidade [{}] '.format(codigos_cidades[maior_indice_acidentes]))
print('A menor indicie de acidentes pertence a cidade [{}] '.format(codigos_cidades[menor_indice_acidentes]))
print('Qual a média de veículos nas cinco cidades juntas [{}] '.format(media_veiculos))
print('Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio. [{}] '.format(media_acidentes200))