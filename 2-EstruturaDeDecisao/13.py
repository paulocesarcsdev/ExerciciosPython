'''
Faça um Programa que leia um número e exiba o dia correspondente da semana. 
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
'''

dia = int(input('Entre com o dia da semana: '))

if(dia == 1):
    print('1-Domingo')
if(dia == 2):
    print('2-Segunda')
if(dia == 3):
    print('3-Terça')
if(dia == 4):
    print('4-Quarta')
if(dia == 5):
    print('5-Quinta')
if(dia == 6):
    print('6-Sexta')
if(dia == 7):
    print('Sabado')
else:
    print('valor inválido')
