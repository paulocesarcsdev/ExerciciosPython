'''
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
Um número primo é aquele que é divisível somente por ele mesmo e por 1.
'''

valor = int(input('Digitie um valor: '))

multiplo = 0

for contador in range(2, valor):
    if (valor % contador == 0):
        print('Multilo de', contador)
        multiplo += 1
        
if(multiplo == 0 and valor >= 2):
    print("Primo")
else:
    print('Tem',multiplo,'multiplo acima de 2 e abaixo de', valor)