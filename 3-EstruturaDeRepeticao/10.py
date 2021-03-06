'''
Faça um programa que receba dois números inteiros e gere os 
números inteiros que estão no intervalo compreendido por eles.
'''

numero_um = int(input("Entre com o primeiro numero: "))
numero_dois = int(input("Entre com o segundo numero: "))

for i in range(numero_um, numero_dois):
    print(i)