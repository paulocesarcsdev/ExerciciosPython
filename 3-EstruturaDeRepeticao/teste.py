
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
print('Média dos demais saltos: {} m'.format(media))
print('\n')
print('Resultado final: ')
print('{}: {} m'.format(nome_atleta,media))