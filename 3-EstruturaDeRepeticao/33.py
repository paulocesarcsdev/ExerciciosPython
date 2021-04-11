'''
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia 
as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas 
informadas, bem como a média das temperaturas.
'''

temperaturas = []

temperatura = float(input('Informe as temperaturas: '))
while(temperatura != 0):
    temperatura = float(input('Informe as temperaturas: '))
    temperaturas.append(temperatura)
    temperatura_maior = max(temperaturas)
    temperatura_menor = min(temperaturas)
    temperatura_media = sum(temperaturas) / len(temperaturas)

print('A maior temperatura foi {} '.format(temperatura_maior))
print('A menor temperatura foi {} '.format(temperatura_menor))
print('A temperatura media foi {} '.format(temperatura_media))