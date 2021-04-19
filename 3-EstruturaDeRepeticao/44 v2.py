'''
O cardápio de uma lanchonete é o seguinte:

Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00

Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. 
Considere que o cliente deve informar quando o pedido deve ser encerrado.

'''
pedidos = []
codigo = -1
quantidade = -1
cardapio = {100:1.20, 101:1.30, 102:1.50, 103:1.20, 104:1.30, 105:1.00}

while(codigo != 0):
    codigo = int(input('Entre com o código do pedido: '))
    quantidade = int(input('Quantidade desejada: '))
    if codigo == 0:
        break
    
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