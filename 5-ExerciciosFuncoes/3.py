'''
Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
'''

def soma(*args):
    resultado = 0
    for i in args:
        resultado += i
    return resultado

print(soma(1,2,3))