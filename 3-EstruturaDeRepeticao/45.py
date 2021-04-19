'''
Em uma eleição presidencial existem quatro candidatos.
Os votos são informados por meio de código. Os códigos utilizados são:

1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco

Faça um programa que calcule e mostre:

    - O total de votos para cada candidato;
    - O total de votos nulos;
    - O total de votos em branco;
    - A percentagem de votos nulos sobre o total de votos;
    - A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.
'''

canditados = [1, 2, 3, 4, 5, 6]
nomes = ['1- kratos', '2 - hitman', '3 - vegeta', '4 - kakashi', '5 - Voto Nulo', '6 - Voto em Branco']
votos = []
voto = True
contador = 0

print("1- kratos | 2 - hitman | 3 - vegeta | 4 - kakashi | 5 - Voto Nulo | 6 - Voto em Branco")
while voto != 0:
    voto = int(input('Entre com o número dos canditados de 1 a 6: '))
    votos.append(voto)
    if voto == 0:
        break
    
for _ in range(len(canditados)):
    print('O total de votos do canditador foi: ', canditados[contador], end='   ')
    if votos.count == 0:
        print('0')
        contador += 1
    else:
        print(votos.count(contador +1))
        contador += 1
        
quantidade_nulo = (votos.count(5) / len(votos)) * 100
quantidade_branco = (votos.count(6) / len(votos)) * 100
print('A porcentagem dos votos nulos {} e Brandos {}'.format(quantidade_nulo,quantidade_branco))