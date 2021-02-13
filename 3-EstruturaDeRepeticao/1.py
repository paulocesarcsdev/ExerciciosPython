'''
Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue
pedindo até que o usuário informe um valor válido.
'''

codicao = True
while(codicao):
    nota = float(input("Entre com o valor da nota, entre zero e dez: "))
    compara_nota1 = nota < 0 
    compara_nota2 = nota > 10
    if(compara_nota1 == compara_nota2):
        print('valido')
        #codicao = True
        break
    if(compara_nota1 != compara_nota2):
        print('Nota invalida por favor continue tentando')
        condicao = False
        continue
    
        
        

