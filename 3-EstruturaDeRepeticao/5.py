'''
Altere o programa anterior permitindo ao usuário informar as 
populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
'''


#populacao_a = 80000
#populacao_b = 200000
contador = 0

populacao_a = int(input("Entre com a População A: "))
taxa_a = float(input("Entre com a taxa A: "))
populacao_b = int(input("Entre com a População B: "))
taxa_b = float(input("Entre com a taxa B: "))

if()


while  (populacao_a <= populacao_b):
    populacao_a += (populacao_a * taxa_a)
    populacao_b += (populacao_b * taxa_b)
    contador += 1
    #print("\n")
    #print(contador)
print('Total  de anos para igualar as populações {}'.format(contador))