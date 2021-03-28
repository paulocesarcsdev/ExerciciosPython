'''
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular
o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.
'''

contador = 2
fatorial = 1

n = int(input("Ente com a quantidade de número que deseja: "))
if(n <= 1):
    print('1')
else:
    while(contador <= n):
        fatorial = fatorial * contador
        contador += 1
    print(fatorial)