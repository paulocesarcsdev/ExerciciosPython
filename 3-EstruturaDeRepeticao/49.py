'''
Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
Exemplo:
  12376489
  => 98467321
'''
sequencia = []

while True:
      numero = int(input('Entre com a sequencia:'))
      
      if numero != 0:
            sequencia.append(numero)
            #sequencia.reverse()
      else:
            break
print('\n')
print(sequencia[::-1])

