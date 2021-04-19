'''
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

https://wiki.python.org.br/ListaDeExercicios
'''
elementos = []
contador = 1
for i in range(5):
    elemento = int(input ('Entre com 5 numeros {} '.format(contador)))
    elementos.append(elemento)
    contador += 1

print('{} '.format(elementos))
