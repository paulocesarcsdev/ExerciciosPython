'''
Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
Imprima no final a soma da série.
'''

def sequ(n):
    aux1 = 2.0
    aux2 = 3.0
    soma = 0
 
    while aux1 <= num:
        print aux1, aux2
        soma = soma + aux1/aux2
        aux1 = aux1 + 1
        aux2 = aux2 + 2
 
    return soma
 
num = input('Digite um valor: ')
while num < 0:
    num = input('Digite um valor positivo: ')
 
res = sequ(num)
print res

#OBS: não testei coloquei para mexer depois.