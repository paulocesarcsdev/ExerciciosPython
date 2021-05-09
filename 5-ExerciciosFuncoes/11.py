'''
Data com mês por extenso.
Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA.
Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
'''

def mesPorExtenso(data):
    dia = int(data[0:2])
    mes = int(data[3:5])
    ano = int(data[6::])
    
    if dia < 1 or dia > 31 or mes > 12 or mes < 1:
        print('Data incorreta')
        return 0
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    
    mesExtenso = str(dia) + ' de ' + meses[mes - 1] + ' de ' + str(ano)
    return mesExtenso

print(mesPorExtenso('10/06/2003'))