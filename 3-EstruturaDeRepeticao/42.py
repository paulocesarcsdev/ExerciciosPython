'''
Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:

Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25

Exemplo de saída do programa:

Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67

'''



valor = float(input('Entre com o valor da divida: '))
contador = 1

for _ in range(5):
    if contador == 1:
        juros = 1
        juros_pagar = 0
    elif contador == 4:
        contador  = 3
        juros = 1.10
    elif contador == 7 or contador == 6:
        contador = 6
        juros = 1.15
    elif contador == 10 or contador == 9:
        contador = 9
        juros = 1.20
    elif contador == 13 or contador == 12:
        contador = 12
        juros = 1.25
    
    
    
    juros_pagar = valor * (juros - 1)
    pagar_juros = valor * juros
    pagamento_parcela = pagar_juros / contador
    print('\n')
    print(round(pagar_juros,2), end= '  ')
    print(round(juros_pagar,2), end= '  ')
    print(round(contador,2), end= '  ')
    print(round(pagamento_parcela,2), end= '  ')
    
    contador += 3