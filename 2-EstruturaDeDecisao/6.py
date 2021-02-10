# Faça um Programa que leia três números e mostre o maior deles.
numeroUm = int(input('Numero um: '))
numeroDois = int(input('Numero dois: '))
numeroTres = int(input('Numero tres: '))

if(numeroUm > numeroDois and numeroUm > numeroTres):
    print("Numero um maior", numeroUm)
elif(numeroDois > numeroUm and numeroDois > numeroTres):
    print('Numero dois maior', numeroDois)
elif(numeroTres > numeroUm and numeroTres > numeroDois):
    print('Numero tres maior', numeroTres)
