'''
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
'''
numeros = []
contador  = 1

for i in range(10):
    numeros.append(int(input('Entre com dez números {}: '.format(contador))))
    contador += 1
    numeros.sort(reverse=True)
    
print('\n')   
print(numeros)