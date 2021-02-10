"""
Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""
g_farenheit = float(input("Entre com a temperatura em Farenheit: "))
celsius = 5 * ((g_farenheit-32) / 9)
print("A temperaura em Celsius: ", celsius)
