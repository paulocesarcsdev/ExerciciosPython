'''
Altere o programa anterior para mostrar no final a soma dos números.
'''

numero_um = int(input("Entre com o primeiro numero: "))
numero_dois = int(input("Entre com o segundo numero: "))
soma = 0
for i in range(numero_um, numero_dois):
    soma += i
    print(soma, end=' ')
    print(i)