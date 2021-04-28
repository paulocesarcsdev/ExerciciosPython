'''
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
'''

idades = []
alturas = []
idade_inversa = []
altura_inversa = []
for i in range(5):
    idade = int(input('Entre com a idade : '))
    idades.append(idade)
    altura = float(input('Entre com altura: '))
    alturas.append(altura)
    
    idade_inversa.append(idade)
    idade_inversa.sort(reverse=True)
    
    altura_inversa.append(altura)
    altura_inversa.sort(reverse=True)
    

print('A idades {} e as alturas {} '.format(idades,alturas))
print('Idade invertida {} Altura invertida {} '.format(idade_inversa, altura_inversa))