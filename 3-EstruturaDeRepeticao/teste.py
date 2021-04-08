total_eleitores = int(input('Numero de eleitores: '))

canditato_A = []
canditato_B = []
canditato_C = []

for i in range(total_eleitores):
    voto = input('Escolha entre os canditador A, B ou C ')
    if(voto == 'A' or voto =='a'):
        canditato_A.append(voto)
    elif(voto == 'B' or voto == 'b'):
        canditato_B.append(voto)
    elif(voto == 'C' or voto == 'c'):
        canditato_C.append(voto)
print('O canditato A  teve: ',len(canditato_A))
print('O canditato B  teve: ',len(canditato_B))
print('O canditato C  teve: ',len(canditato_C))