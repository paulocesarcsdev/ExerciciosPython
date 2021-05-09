def data(data):
    dia = int(data[0:2])
    mes = int(data[3:5])
    ano = int(data[6::])

    if dia < 1 or dia > 31 or mes > 12 or mes < 1:
        print('Data inválida')
        return 0

    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']    

    novaData = str(dia) + ' de ' + meses[mes - 1] +' de ' + str(ano)
    return novaData
print(data('10/12/2000'))