''''
Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

'''
def numeroDigitado(n):
    return len(str(n))

numero = int(input('Entre com valor: '))

print(numeroDigitado(numero))

