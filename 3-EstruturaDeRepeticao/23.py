'''
Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. 
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. 
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
'''
valor = int(input('Digitie um valor: '))

multiplo = 0

for contador in range(2, valor):
    if (valor % contador == 0):
        print('Multiplo de {}'.format(contador))
        multiplo += 1
    print('Numero de divisões {} '.format(contador))
    
    if(multiplo == 0 and valor >= 2):
        print("Primo")
    else:
        print('Tem {} multiplo acima de 2 e abaixo de {}'.format(multiplo,valor) )