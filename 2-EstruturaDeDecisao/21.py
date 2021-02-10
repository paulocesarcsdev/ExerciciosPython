'''
Faça um Programa para um caixa eletrônico.
O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na máquina.
a. Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
b. Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
'''

saque = int(input('Entre com o valor que deseja sacar, R$: '))

if(saque < 10 or saque <= 600):
    valor_cem = int(saque / 100)
    saque = saque - (valor_cem * 100)

    valor_cinquenta = int(saque / 50)
    saque = saque - (valor_cinquenta * 50)

    valor_dez = int(saque / 10)
    saque = saque - (valor_dez * 10)

    valor_cinco = int(saque / 5)
    saque = saque - (valor_cinco * 5)

    valor_um = saque

    if(valor_cem == 1 or valor_cem > 1):
        print('nota de cem', valor_cem)
    if(valor_cinquenta == 1 or valor_cinquenta > 1):
        print('nota de cinquenta', valor_cinquenta)
    if(valor_dez == 1 or valor_dez > 1):
        print('nota de dez', valor_dez)
    if(valor_cinco == 1 or valor_cinco > 1):
        print('nota de cinco', valor_cinco)
    if(valor_um == 1 or valor_um > 1):
        print('nota de um', valor_um)
else:
    print('Não pode sacar esse valor: ')
