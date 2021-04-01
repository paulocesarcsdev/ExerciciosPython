'''
Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

'''
#Essa opção já foi adicionada no  21.py
valor = int(input('Digitie um valor: '))

multiplo = 0

for contador in range(2, valor):
    if (valor % contador == 0):
        print('Multiplo de {}'.format(contador))
        multiplo += 1
        
if(multiplo == 0 and valor >= 2):
    print("Primo")
else:
    print('Tem {} multiplo acima de 2 e abaixo de {}'.format(multiplo,valor) )