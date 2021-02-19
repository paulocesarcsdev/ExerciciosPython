'''
Faça um programa que leia e valide as seguintes informações:
a. Nome: maior que 3 caracteres;
b. Idade: entre 0 e 150;
c. Salário: maior que zero;
d. Sexo: 'f' ou 'm';
e. Estado Civil: 's', 'c', 'v', 'd';
'''

#nome = input('Entre com o nome: ')
#idade = int(input('Entre com a idade: '))
#salario = float(input('Entre com o salário: '))
#sexo = input('Entre com o sexo: ')
#estado_civil = input('Entre com o estado civil: ')

validaro = True
while(validador):
    nome = input('Entre com o nome: ')
    if(len(nome) > 3):
        print('Nome {} maior q 3'.format(nome))
    else:
        print('Nome {} menor que 3 '.format(nome))
        
    idade = int(input('Entre com a idade: '))
    if(idade > 0 and idade < 150):
        print('Idade {} entre 0 e 150'.format(idade))
    else:
        print('Idade não está entre 0 150'.format(idade))
    salario = float(input('Entre com o salário: '))
    if(salario > 0):
        print('O salario {} maior que zero: '.format(salario))
    else:
        print('O salario {} e menor que zero: '.format(salario))
    sexo = input('Entre com o sexo: ')
    if(sexo == 'f' or sexo == 'F'):
        print('O {} sexo feminino '.format(sexo))
    elif(sexo == 'm' or sexo == 'M'):
        print('O {} sexo masculino'.format(sexo))
    else:
        print('Sexo inválido tente novamente')
    estado_civil = input('Entre com o estado civil: ')    
    if(estado_civil == 's' or estado_civil == 'S'):
        print('Estado civil {} solteiro: '.format(estado_civil))
    elif(estado_civil == 'c' or estado_civil == 'C'):
        print('Estado civil {} casado: '.format(estado_civil))
    elif(estado_civil == 'v' or estado_civil == 'V'):
        print('Estado civil {} viuvo(a): '.format(estado_civil))
    elif(estado_civil == 'd' or estado_civil == 'D'):
        print('Estado civil {} divorcidado(a): '.format(estado_civil))
    else:
        print('Estado civil inválido tente novamente: ')
    print('Para sair escreva sair: ')
