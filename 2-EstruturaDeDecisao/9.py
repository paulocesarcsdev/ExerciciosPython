# Faça um Programa que leia três números e mostre-os em ordem decrescente.
numeroUm = int(input('Numero um: '))
numeroDois = int(input('Numero dois: '))
numeroTres = int(input('Numero tres: '))


# Exibe o maior
if(numeroUm > numeroDois and numeroUm > numeroTres):
    print("Numero um maior", numeroUm)
if(numeroDois > numeroUm and numeroDois > numeroTres):
    print('Numero dois maior', numeroDois)
if(numeroTres > numeroUm and numeroTres > numeroDois):
    print('Numero tres maior', numeroTres)

# Exibe numero do meio
if(numeroUm < numeroDois and numeroUm > numeroTres):
    print("Numero um meio", numeroUm)
if(numeroDois < numeroUm and numeroDois > numeroTres):
    print('Numero dois meio', numeroDois)
if(numeroTres < numeroUm and numeroTres > numeroDois):
    print('Numero tres meio', numeroTres)


# Exibe o menor
if(numeroUm < numeroDois and numeroUm < numeroTres):
    print("Numero um menor", numeroUm)
if(numeroDois < numeroUm and numeroDois < numeroTres):
    print('Numero dois menor', numeroDois)
if(numeroTres < numeroUm and numeroTres < numeroDois):
    print('Numero tres menor', numeroTres)
