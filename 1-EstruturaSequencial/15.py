"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para 
o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
a. salário bruto.
b. quanto pagou ao INSS.
c. quanto pagou ao sindicato.
d. o salário líquido.
e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""
valor_hora = float(input("Quanto ganha por hora? :"))
numero_hora = float(input("Quantas horas trabalhadas no mês? : "))
salario_mes = (valor_hora * numero_hora)
# IR
impostoDe_renda = 0.11
desconto_impostoRenda = (salario_mes * impostoDe_renda)
# INSS
inss = 0.08
desconto_inss = (salario_mes - desconto_impostoRenda) * inss
# Sindicato
sindicato = 0.05
desconto_sindicato = (salario_mes - desconto_inss) * sindicato
# Salário Bruto
total_desconto = (desconto_impostoRenda + desconto_inss + desconto_sindicato)
salario_bruto = salario_mes - total_desconto
print("Salário Bruto : R$", salario_mes)
print("- IR (11%) : R$", desconto_impostoRenda)
print("- INSS (8%) : R$", desconto_inss)
print("- Sindicato ( 5%) : R$", desconto_sindicato)
print("= Salário Liquido : R$", salario_bruto)
print("Total desconto", total_desconto)
