'''
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, 
o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que 
pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. 
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. 
Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, 
do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes

'''

codigos = []
alturas = []
pesos = []
codigo = True
contador = 1


print('Para sair presione 0 ')
while(codigo != 0):
    codigo = int(input('Entre com o código do cliente {} : '.format(contador)))
    codigos.append(codigo)
    altura = float(input('Entre com altura cm: '))
    alturas.append(altura)
    peso = float(input('Entre com peso kg : '))
    pesos.append(peso)
    contador += 1
    
    #Calculos
    
    maior_altura = max(alturas)
    menor_altura = min(alturas)
    maior_peso = max(pesos)
    manor_peso = min(pesos)
                
    for i in codigos:
        print('Códigos {} '.format(i,'\n'))

#print('Codigo ',codigos)
print('Maior altura cm: ', maior_altura)
print('Manor altura cm: ', menor_altura)
print('Mais gordo kg: ', maior_peso)
print('Mais magro kg: ', manor_peso)
print('Media das alturas cm :',sum(alturas) / len(alturas) )
print('Media dos pesos kg: ', sum(pesos) / len(pesos))