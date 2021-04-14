ano_inicial = 1995
ano_atual  = 1996
contador  = 0
salario = 1000
novo_salario = 0


for i in range(ano_inicial, ano_atual):
    contador += 1
    aumento_salario = contador * 1.5 * 100 
    novo_salario += salario + aumento_salario
    
print(novo_salario)