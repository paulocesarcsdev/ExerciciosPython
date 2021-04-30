'''
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).
Após esta entrada de dados, faça:
    a. Mostre a quantidade de valores que foram lidos;
    b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
    c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
    d. Calcule e mostre a soma dos valores;
    e. Calcule e mostre a média dos valores;
    f. Calcule e mostre a quantidade de valores acima da média calculada;
    g. Calcule e mostre a quantidade de valores abaixo de sete;
    h. Encerre o programa com uma mensagem;
'''
notas = []
notas_inverso = []
media = 0
conta_valor_media = 0
contar_menor_sete = 0
maior = 7

print('=-=-=-=-==-=-Para sair -1=-=-=-=-==-=- ')
while True:
    nota = float(input('Entre com as notas: '))
    if nota < 0:
        break
    notas.append(nota)
    notas_inverso = notas.copy()
    notas_inverso = notas_inverso[::-1]
    media = sum(notas) / len(notas)
    
for j in notas:
    if j > media:
        conta_valor_media += 1
            
    if j < maior:
        contar_menor_sete += 1
    
print('a. Mostre a quantidade de valores que foram lidos; {} '.format(len(notas)))
print('b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro; {} '.format(notas))
print('c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro; ')
for i in notas_inverso:
    print(i)
print('d. Calcule e mostre a soma dos valores; {} '.format(sum(notas)))
print('e. Calcule e mostre a média dos valores; {} '.format(media))
print('f. Calcule e mostre a quantidade de valores acima da média calculada; {} '.format(conta_valor_media))
print('g. Calcule e mostre a quantidade  de valores  abaixo de sete; {} '.format(contar_menor_sete))