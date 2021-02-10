'''
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
a) "Telefonou para a vítima?"
b) "Esteve no local do crime?"
c) "Mora perto da vítima?"
d) "Devia para a vítima?"
e) "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente".
'''

print('Responta as perguntas: ')

contador = 0

print("Telefonou para a vítima?")
a = int(input('Aperte 1 para sim 0 para não: '))
print("Esteve no local do crime?")
b = int(input('Aperte 1 para sim 0 para não: '))
print("Mora perto da vítima?")
c = int(input('Aperte 1 para sim 0 para não: '))
print("Devia para a vítima?")
d = int(input('Aperte 1 para sim 0 para não: '))
print("Já trabalhou com a vítima?")
e = int(input('Aperte 1 para sim 0 para não: '))
contador = (a + b + c + d + e)

if(contador == 2):
    print("Suspeita")
if(contador == 3 or contador == 4):
    print("Cúmplice")
if(contador == 5):
    print('"Assassino"')
if(contador == 1 or contador == 0):
    print("Inocente")