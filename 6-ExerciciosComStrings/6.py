'''
Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.
    Data de Nascimento: 29/10/1973
    Você nasceu em  29 de Outubro de 1973.
'''

def nascimento(data):
    meses = ['Janeiro', 'Fevereiro', 'Março',  'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro','Outubro', 'Novembro', 'Dezembro']
    dia = data[:2]
    mes = int(data[3:5])
    atual = meses[mes]
    ano = data[6:]
    print('Você nasceu em {} de {} de {}'.format(dia,atual,ano))
    

print('Data de nascimento (dd/mm/aaaa)')
data = str(input('Entre com a data de nascimento: '))
nascimento(data)