'''
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
a. par ou ímpar;
b. positivo ou negativo;
c. inteiro ou decimal.
'''

numero_um = float(input('Entre com o primeiro numero: '))
numero_dois = float(input('Entre com o segundo numero: '))

resultado = 0
print('numero um', numero_um)
print('numero dois', numero_dois)


print('adição  + ')
print('subitação - ')
print('divisão / ')
print('multiplicação * ')
operacao = input('Qual operação deseja realizar? ')

if(operacao == '+'):
    resultado = numero_um + numero_dois
    print('resultado', resultado)
if(operacao == '-'):
    resultado = numero_um - numero_dois
    print('subtracao', resultado)
if(operacao == '/'):
    resultado = numero_um / numero_dois
    print('divisao', resultado)
if(operacao == '*'):
    resultado = numero_um * numero_dois
    print('multiplicao', resultado)
if(resultado % 2 == 0):
    print('par')
else:
    print('impar')
if(resultado > 0):
    print('positivo')
else:
    print('negativo')
resultado_ = round(resultado)
if(resultado_ != resultado):
    print('decimal')
else:
    print('inteiro')
