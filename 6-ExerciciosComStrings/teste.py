meses = ['Janeiro', 'Fevereiro', 'Março',  'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro','Outubro', 'Novembro', 'Dezembro']






data = str(input('Entre com a data de nascimento: '))

dia = data[:2]
mes = int(data[3:5])
atual = meses[mes]
ano = data[6:]

print('Você nasceu em {} de {} de {}'.format(dia,atual,ano))
