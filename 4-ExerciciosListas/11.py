'''
Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
'''

vetor_a = []
vetor_b = []
vetor_c = []
vetor_d = []

for i in range(10):
    a = int(input('Vetor A: '))
    vetor_a.append(a)
    b = int(input('Vetor B: '))
    vetor_b.append(b)
    c = int(input('Vetor C: '))
    vetor_c.append(c)
    
    vetor_d.append(a)
    vetor_d.append(b)
    vetor_d.append(c)
    
print(vetor_a)
print(vetor_b)
print(vetor_c)