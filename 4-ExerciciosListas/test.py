notas = []
notas_inverso = []
soma = 0
sair = 0
media = 0
conta_valor_media = 0
contar_menor_sete = 0
maior = 7

quantidade_numeros =  int(input('Entre com a quantidade de número: '))
for i in range(quantidade_numeros):
    nota = float(input('Entre com as notas: '))
    notas.append(nota)
    soma += nota
    notas_inverso = notas.copy()
    notas_inverso = notas_inverso[::-1]
    media = soma / quantidade_numeros
    
for j in notas:
    if j > media:
        conta_valor_media += 1
            
    if j < maior:
        contar_menor_sete += 1
    
print('a. Mostre a quantidade de valores que foram lidos; {} '.format(quantidade_numeros))
print('b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro; {} '.format(notas))
print('c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro; ')
for i in notas_inverso:
    print(i)
print('d. Calcule e mostre a soma dos valores; {} '.format(soma))
print('e. Calcule e mostre a média dos valores; {} '.format(media))
print('f. Calcule e mostre a quantidade de valores acima da média calculada; {} '.format(conta_valor_media))
print('g. Calcule e mostre a quantidade  de valores  abaixo de sete; {} '.format(contar_menor_sete))