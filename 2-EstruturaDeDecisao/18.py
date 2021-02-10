'''
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
'''

print('Entre com Dia/Mês/Ano')

dia = int(input('Entre com o dia: '))
mes = int(input('Entre com o mês: '))
ano = int(input('Entre com o ano: '))

if(dia <= 31 and mes <= 12):
    print('A data informada e válida')
else:
    print('Não e válida')
