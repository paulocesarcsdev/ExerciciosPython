'''
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:

a. 326 = 3 centenas, 2 dezenas e 6 unidades
b. 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

'''

#numero = int(input('Entre com um valor inteiro menor que 1000: '))
#arquivo = open('arquivo.txt', 'r', encoding="utf-8")
dados = open('arquivo.txt', 'r', encoding='utf-8')

#aux = []
#aux = file

print(dados.read())
'''
centena = aux // 100

dezena = aux // 10 % 10

unidade = aux % 10


print('Centena', centena)
print('Dezena', dezena)
print('Unidade', unidade)
'''
