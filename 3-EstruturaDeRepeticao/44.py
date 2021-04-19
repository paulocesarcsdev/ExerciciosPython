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

cardapio = ['Cachorro Quente', 'Bauru Simples', 'Bauru com ovo', 'Hambúrguer', 'Cheeseburguer', 'Refrigerante']
codigos = [100, 101, 102, 103, 104, 105]
preco = [1.20, 1.30, 1.50, 1.20, 1.30, 1.00]
codigo = True
numero_pedido = 1
pedidos = []

while codigo != 0:
    print('Número do pedido º{}'.format(numero_pedido))
    codigo = int(input('Entre com o cógido: '))
    if codigo == 0:
        break
    else:
        while codigo not in codigos:
            print("[Este código não corresponde a nenhum alimento.]")
            codigo = int(input("Digite o código do alimento: "))
        
        indice = codigos.index(codigo)
        quantidade = int(input('Entre com a quantidade: '))
        preco_pedido = preco[indice] * quantidade
        pedidos.append(preco_pedido)
    numero_pedido += 1
    
sair = 0
for _ in range(numero_pedido - 1):
    print('O pedido º',sair +1, "= R$", round(pedidos[sair],2))
    sair += 1
print('O valor total R$ {}', round(sum(pedidos)))
