'''
Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros.
Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída.
Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M.
Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M.
Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.
'''

def conversao(hora, minuto):
    if hora > 12:
        hora_pm = hora - 12
        print('P.M {}:{} '.format(hora_pm,minuto))
    else:
        print('A.M {}:{} '.format(hora,minuto))

def saida():
    print(conversao())




while True:
    horas = int(input('Entre com a hora no formato 24 horas: '))
    if horas < 0:
        break
    minutos = int(input('Entre com os minutos: '))
    convertido = conversao(horas,minutos)
