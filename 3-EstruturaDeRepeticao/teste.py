pedidos = []
codigo = -1
quantidade = -1

while(codigo != 0 or quantidade != 0):
    codigo = int(input('Entre com o código do pedido: '))
    quantidade = int(input('Quantidade desejada: '))
    
    if codigo == 100:
        cachorro_quente = quantidade * 1.20
        pedidos.append(cachorro_quente)
    elif codigo == 101:
        bauru_simples = quantidade * 1.30
        pedidos.append(bauru_simples)
    elif codigo == 102:
        bauru_com_ovo = quantidade * 1.50
        pedidos.append(bauru_com_ovo)
    elif codigo == 103:
        hambúrguer = quantidade * 1.20
        pedidos.append(hambúrguer)
    elif codigo == 104:
        cheeseburguer = quantidade * 1.30
        pedidos.append(cheeseburguer)
    elif codigo == 105:
        refrigerante = quantidade * 1.00
        pedidos.append(refrigerante)
    
    valor_lanche = sum(pedidos)
    print('Valor lanche R$: {} '.format(valor_lanche))