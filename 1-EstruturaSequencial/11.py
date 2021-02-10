"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a. o produto do dobro do primeiro com metade do segundo .
b. a soma do triplo do primeiro com o terceiro.
c. o terceiro elevado ao cubo.
"""
primeiro = int(input("Entre com o número inteiro: "))
segundo = float(input("Entre com o número real: "))

# A
metade = segundo / 2
produto = (primeiro * 2) + metade
print("A: ", produto)

# B
triplo = primeiro * 3
soma_triplo = primeiro + produto
print("B: ", soma_triplo)

# C
cubo = produto ** 3
print("C :", cubo)
