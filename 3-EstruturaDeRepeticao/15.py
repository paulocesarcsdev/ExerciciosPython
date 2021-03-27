'''
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
Faça um programa capaz de gerar a série até o n−ésimo termo.
'''


n = int(input('Entre com o valor: '))

ultimo = 1
penultimo = 1

if n <= 2:
     print('1')
else:
    contador = 3
    while(contador <= n):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        contador += 1
        print(termo, end =' ')

