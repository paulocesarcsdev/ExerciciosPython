'''
Faça um programa que leia e valide as seguintes informações:
a. Nome: maior que 3 caracteres;
b. Idade: entre 0 e 150;
c. Salário: maior que zero;
d. Sexo: 'f' ou 'm';
e. Estado Civil: 's', 'c', 'v', 'd';
'''

nome = input('Entre com o nome: ')
idade = int(input('Entre com a idade: '))
#salario = float(input('Entre com o salário: '))
#sexo = input('Entre com o sexo: ')
#estado_civil = input('Entre com o estado civil: ')

contador = 0

#print(tamanho_nome)
teste = False
while(True):
    if(len(nome) > 3):
        print('O nome {} e valido possui mais de três caracteres: '.format(nome))
        break
    else:
        print('O nome {} e invalido possui menos de três caracteres: '.format(nome))
        
    #idade = int(input('Entre com a idade: '))
    if(idade < 0) or (idade > 150):
        print('A idaide {} está entre 0 e 150'.format(idade))
    else:
        print('A idaide {} não está entre 0 e 150'.format(idade))
        
    if(salario > 0):
        print('O salário {} maior que zero')
    else:
        print('O salário {} e menor que')



#print(nome)
#print(idade)
#print(salario)
#print(sexo)
#print(estado_civil)