'''
Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados.
O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa
que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe
a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média).
Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados.
O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m

Resultado final:
Rodrigo Curvêllo: 5.9 m


'''


saltos = []
saltos_aux = []
nome_atleta = input('Entre com o nome do atleta: ')

conta_salto = 1
for i in range(5):
    print('Entre com o salto {}: '.format(conta_salto))
    salto = float(input('A distância do slto foi: '))
    saltos.append(salto)
    conta_salto += 1
    saltos_aux = saltos.copy()
 
del saltos_aux[-1]
del saltos_aux[0]
melhor_salto = max(saltos_aux)
pior_salto = min(saltos_aux)
media = sum(saltos_aux) / len(saltos_aux)


print('\n')
print('Primeiro Salto: {} m'.format(saltos[0]))
print('Segundo Salto: {} m'.format(saltos[1]))
print('Terceiro Salto: {} m'.format(saltos[2]))
print('Quarto Salto: {} m'.format(saltos[3]))
print('Quinto Salto: {} m'.format(saltos[4]))
print('\n')

print('Melhor salto: {} m'.format(melhor_salto))
print('Pior salto: {} m'.format(pior_salto))
print('Média dos demais saltos: {} m'.format(round(media,2)))
print('\n')
print('Resultado final: ')
print('{}: {} m'.format(nome_atleta,round(media,2)))