"""
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
"""
altura = float(input("Entre com altura: "))
peso = float(input("Entre com o peso: "))
peso_ideal = (72.7*altura) - 58
print("Seu peso: ", peso)
print("Peso ideal:", peso_ideal)
perder_peso = (peso - peso_ideal)
print("Necessário perder:", perder_peso)
