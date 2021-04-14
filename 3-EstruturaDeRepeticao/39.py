'''
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
    a) Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
    b) Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
    c) A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. 
        Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo 
        que o usuário digite o salário inicial do funcionário.
'''


ano_inicial = 1995
ano_atual  = 1999
contador  = 0
salario = 1000
novo_salario = 0
aumento_salario = 0


for i in range(ano_inicial, ano_atual):
    contador += 1
    if(ano_inicial > 1997):
        dobro =  aumento_salario * aumento_salario
    aumento_salario = contador * 0.015 * 100 
    novo_salario += salario + aumento_salario

print('Salario inicial', salario, 'Ano do primeiro salario', ano_inicial)
print('Salario Atual', novo_salario, 'Salario ano atual', ano_atual)
print('Aumento', aumento_salario)