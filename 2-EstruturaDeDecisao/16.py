'''
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
a. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
b. Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
d. Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''
import math

print('Entre com os dados da equação de segundo grau ax2 + bx + c ')
a = int(input('Entre com o coeficiente A: '))
b = int(input('Entre com o coeficiente B: '))
c = int(input('Entre com o coeficiente C: '))

delta = b**2 - 4 * (a) * (c)
raiz_delta = math.sqrt(abs(delta))

if(a == 0):
    print('Não e uma equação do segundo grau A = 0')
elif(delta < 0):
    print('delta calculado negativo, a equação não possui raizes reais.')
    print('delta', delta)
elif(delta == 0):
    print('delta calculado igual a zero a equação possui apenas uma raiz real')
    y1 = (- b + raiz_delta) / 2 * a
    print("y'=", y1)
elif(delta > 0):
    print('delta for positivo, a equação possui duas raiz reais')
    y1 = (- b + raiz_delta) / 2 * a
    y2 = (- b - raiz_delta) / 2 * a
    print("y'=", y1)
    print("y'=", y2)
