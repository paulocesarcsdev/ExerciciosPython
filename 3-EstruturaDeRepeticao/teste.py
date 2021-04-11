'''
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui 
uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. 
O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias.
Um valor zero deve ser informado pelo operador para indicar o final da compra. 
O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, 
para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, 
para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:

Lojas Tabajara 
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
...

'''
while(True):
    valor_produto = []
    contador = 1
    total_pagar = 0
    valor_compra = True

    #saida = float(input('Para continuar aperte 1 para sair aperte 0: '))
    while(valor_compra != 0):
        valor_compra = float(input('Entre com o valor da compra: '))
        valor_produto.append(valor_compra)
        total_pagar = sum(valor_produto)


    print('O valor dos produtos foi R$ {}'.format(total_pagar))
    pagamento = float(input('Informe quanto o cliente pago ao caixa: R$: '))
    
    while(pagamento < total_pagar):
        pagamento = float(input('Dinheiro insuficiente valor R$ {} abaixo da compra, tente novamente: '.format(pagamento)))
    
    troco = pagamento - total_pagar
            
    print('Lojas Tabajara')    
    for i in (valor_produto):
        print('Produto {}: R$ {}'.format(contador,i))
        contador += 1
    print('Total: R$ {}'.format(total_pagar))
    print('Dinheiro R$ {}'.format(total_pagar))
    print('Troco R$ {} '.format(troco))
