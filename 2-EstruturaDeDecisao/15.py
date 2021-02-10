'''
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
'''

lado_a = int(input('Entre com o lado A: '))
lado_b = int(input('Entre com o lado B: '))
lado_c = int(input('Entre com o lado C: '))

if(lado_a == lado_b and lado_a == lado_c and lado_b == lado_c):
    print('Triângulo Equilátero: três lados iguais;')
if(lado_a == lado_b or lado_a == lado_c or lado_b == lado_c):
    print('Triângulo Isósceles: quaisquer dois lados iguais')
if(lado_a != lado_b or lado_a != lado_c or lado_b != lado_c):
    print('Triângulo Escaleno: três lados diferentes;')
else:
    print('Não forma trinagulo')
