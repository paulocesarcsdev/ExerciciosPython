'''
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
sabendo que a decisão é sempre pelo mais barato.
'''
produtoUm = int(input('Preço produto um: '))
produtoDois = int(input('Preço produto dois: '))
produtoTres = int(input('Preço produto tres: '))

if(produtoUm < produtoDois and produtoUm < produtoTres):
    print("O produto um mais barato custa: ", produtoUm)
elif(produtoDois < produtoUm and produtoDois < produtoTres):
    print("O produto dois mais barato custa: ", produtoDois)
elif(produtoTres < produtoUm and produtoTres < produtoDois):
    print("O produto tres mais barato custa: ", produtoTres)
