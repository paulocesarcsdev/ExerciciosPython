"""
Faça um programa para uma loja de tintas. O programa deverá pedir o 
tamanho em metros quadrados da área a ser pintada. Considere que a 
cobertura da tinta é de 1 litro para cada 3 metros quadrados e que 
a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""
metros_quadrados = float(
    input("Tamanho em metros quadrados da área a ser pintada. "))
cobertura_da_tinta = 3 * metros_quadrados
lata_de_tintaL = 18
custo_lata = 80.00
total_latas = (cobertura_da_tinta // lata_de_tintaL)
custo_total = (total_latas * custo_lata)
print("Quantidade de necessária: ", cobertura_da_tinta)
print("Quantidade de latas: ", total_latas)
print("Valor total das latas:R$", custo_total)
