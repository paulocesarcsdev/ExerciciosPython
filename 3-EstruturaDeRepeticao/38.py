'''
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, 
o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que 
pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. 
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. 
Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, 
do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes

'''

clientes = []
codigo = 1
contador = 1

maior_altura = 0
menor_altura = 0
maior_peso = 0
manor_peso = 0

while(codigo):
    if codigo:
        codigo = int(input('Entre com o código do cliente {} : '.format(contador)))
        altura = float(input('Entre com altura cm: '))
        peso = float(input('Entre com peso kg : '))
        clientes.append( {'Codigo': codigo, 'Altura': altura, 'Peso': peso} )
        contador += 1
        
      #Calculos
    for i in clientes:
        if i['Altura'] > maior_altura:
            codigo_maior = i['Codigo']
            maior_altura = i['Altura']
        if i['Altura'] < menor_altura:
            codigo_menor = i['Codigo']
            menor_altura = i['Altura']
        if i['Peso'] > maior_peso:
            codigo_maiorPeso = i['Codigo']
            maior_peso = i['Peso']
        if i['Peso'] < menor_altura:
            codigo_menorPeso = i['Codigo']
            codigo_menor = i['Peso']
            
print('Maior altura cm: ', maior_altura)
print('Menor altura cm: ', menor_altura)
print('Mais gordo kg: ', maior_peso)
print('Mais magro kg: ', manor_peso)