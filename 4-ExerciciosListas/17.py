'''
Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
O resultado do atleta será determinado pela média dos cinco valores restantes.
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas
pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos.
O programa deve ser encerrado quando não for informado o nome do atleta.
A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo
 
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m

'''

saltos = []
contador_salto = 1


nome = input('Entre com o nome do atleta: ')
for i in range(5):
    salto = float(input('Entre com distância {}º '.format(contador_salto)))
    saltos.append(salto)
    media_saltos = sum(saltos) / len(saltos)
    contador_salto += 1
    
print('Resultado final:')
print('Atleta: {} '.format(nome))
for j in saltos:
    print(j,end=' - ')

print()
print('Média dos saltos: {} m'.format(media_saltos))