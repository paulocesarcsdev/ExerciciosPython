'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
 -salários até R$ 280,00 (incluindo) : aumento de 20%
 -salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
 -salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
 -salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
 -salário antes do reajuste;
 -percentual de aumento aplicado;
 -valor do aumento;
 -novo salário, após o aumento.
'''

salario_atual = float((input('Salário atual: ')))
# print(salario_atual)

#salario = float(input('Entre com o salário do colaborador: '))

if(salario_atual <= 280.00):
    salario_reajuste = salario_atual * 0.2
    valor_aumento = salario_atual - salario_reajuste
    novo_salario = salario_atual + valor_aumento
    print('Salário antes do reajuste R$', salario_atual)
    print('Percentual de aumento aplicado 20%')
    print('Valor aumento : R$', valor_aumento)
    print('Novo salário, após o aumento: R$', novo_salario)
elif(salario_atual > 280.00 and salario_atual <= 700.00):
    salario_reajuste = salario_atual * 0.15
    valor_aumento = salario_atual - salario_reajuste
    novo_salario = salario_atual + valor_aumento
    print('Salário antes do reajuste R$', salario_atual)
    print('Percentual de aumento aplicado 15%')
    print('Valor aumento : R$', valor_aumento)
    print('Novo salário, após o aumento: R$', novo_salario)
elif (salario_atual > 700.00 and salario_atual <= 1500.00):
    salario_reajuste = salario_atual * 0.10
    valor_aumento = salario_atual - salario_reajuste
    novo_salario = salario_atual + valor_aumento
    print('Salário antes do reajuste R$', salario_atual)
    print('Percentual de aumento aplicado 10%')
    print('Valor aumento : R$', valor_aumento)
    print('Novo salário, após o aumento: R$', novo_salario)
elif (salario_atual > 1500.00):
    salario_reajuste = salario_atual * 0.05
    valor_aumento = salario_atual - salario_reajuste
    novo_salario = salario_atual + valor_aumento
    print('Salário antes do reajuste R$', salario_atual)
    print('Percentual de aumento aplicado 5%')
    print('Valor aumento : R$', valor_aumento)
    print('Novo salário, após o aumento: R$', novo_salario)
