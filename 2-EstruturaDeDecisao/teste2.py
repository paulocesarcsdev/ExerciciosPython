saque = int(input('Entre com o valor que deseja sacar, R$: '))

if(saque > 10 or saque < 600):
    valor_cem = int(saque / 100)
    saque = saque - (valor_cem * 100)

    valor_cinquenta = int(saque / 50)
    saque = saque - (valor_cinquenta * 50)

    valor_dez = int(saque / 10)
    saque = saque - (valor_dez * 10)

    valor_cinco = int(saque / 5)
    saque = saque - (valor_cem * 5)

    valor_um = saque
    print('valor um', valor_um)

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
