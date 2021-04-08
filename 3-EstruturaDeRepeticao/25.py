'''
Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar
se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer 
se a turma é jovem, adulta ou idosa, conforme a média calculada.
'''

numero_pessoas = int(input("Entre com o número de pessoas: "))
soma_total = 0
for i in range(numero_pessoas):
    idade = int(input("Entre com a idade das pessoas: "))
    soma_total += idade
    media_idade = (soma_total / numero_pessoas)
if media_idade > 0 and media_idade <= 25 :
    print('Turma jovem media de idade {}'.format(media_idade))
elif media_idade > 26 and media_idade <= 60:
    print('Turma adulta media de idade {}'.format(media_idade))
elif media_idade >= 60:
    print('Truma idosa idade superior a 60, {}'.format(media_idade))