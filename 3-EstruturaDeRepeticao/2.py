'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
mostrando uma mensagem de erro e voltando a pedir as informações.
'''

while(True):
    nome = input('Entre com o nome de usuário: ')
    senha = input('Entre com a senha de usuário: ')
    if(nome != senha):
        print('valida, parabéns =) ')
        break
    else:
        print('[erro] senha igual precisa ser diferente repita novamente: ')
        
