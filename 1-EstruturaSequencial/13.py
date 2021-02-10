"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
a. Para homens: (72.7*h) - 58
b. Para mulheres: (62.1*h) - 44.7
"""
altura = float(input("Entre com altura: "))
peso = float(input("Entre com o peso: "))


peso_ideal = (72.7*altura) - 58
print("Seu peso: ", peso)
print("Peso ideal homem:", peso_ideal)


peso_ideal = (62.1*altura) - 44.7
print("Seu peso: ", peso)
print("Peso ideal mulher:", peso_ideal)
