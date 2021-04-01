'''
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
'''


numeros = int(input('Entre com a quantidade de números: '))
numeros_lista = []
contador = 0
num = 0

while(contador <= numeros): 
    num = int(input('Entre com os números: '))
    if(num >= 0 and num <= 1000):
        numeros_lista.append(num)
        
        numeros_lista.sort()
        
        menor = min(numeros_lista)
        maior = max(numeros_lista)
        soma_maiorMenor = menor + maior
        
        contador += 1
    else:
        print('apenas números entre 0 e 1000.')
        
print('valores na lista', numeros_lista)
print('menor valor = ', menor)
print('maior valor = ', maior)
print('soma dos valores =', soma_maiorMenor)