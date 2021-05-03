'''
Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
'''

def somar(*args):
    resultado = 0
    resultado = sum(*args)
    return resultado


valores = []
for i in range(3):
    valor = int(input('Entre com 3 valores: '))
    valores.append(valor)

print(somar(valores))