'''
Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta.
O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para
a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou.
O programa deverá então exibir o valor a ser pago na tela.
Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja
informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo
o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia.
O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação.
Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
'''

def valorPagamento(valor_receber, dias_atraso):
    juros = 0
    if dias_atraso == 0:
        return valor_receber
    else:
        juros = 0.1 * dias_atraso
        return valor_receber + ((3 * valor_receber)/ 100) + juros
    

contador = 0
total = 0

while True:
    pagamento = float(input('Quando deve pagar: '))
    if pagamento == 0:
        break
    dias = int(input('Digite quantidade de dias de atraso: '))
    total += valorPagamento(pagamento,dias)
    contador += 1
    
print('Quantidade total  {} '.format(contador) )
print('Valor das prestações R$ {} '.format(total))