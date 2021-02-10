'''
Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
'''
ano = int(input('Entre com o ano: '))

print('ano', ano)

quatro = ano % 4
quatro_centos = ano % 400
cem = ano % 100
aux = -1

#quatro_centos = quatro_centos * aux + quatro_centos
#cem = cem * aux + cem

if(quatro == 0 and quatro_centos == 0 and cem == 0):
    print('Ano bissexto')
else:
    print('Ano nao-bissexto')
