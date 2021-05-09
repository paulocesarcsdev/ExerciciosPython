'''
Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados.
Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória.
Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.
'''

from random import sample


def embaralha(palavra):
    palavra_lista = sample(palavra,len(palavra))
    #palavra_string = ''.join(palavra)
    print(palavra_lista)
    #print(palavra_string.lower())
    
palavra = input('Entre com qualquer nome: ')
embaralha(palavra)