'''
Faça um Programa que leia dois vetores com 10 elementos cada.
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
'''

vetor_a = []
vetor_b = []
vetor_c = []

for i in range(10):
    a = int(input('Vetor A:'))
    vetor_a.append(a)
    b = int(input('Vetor B: '))
    vetor_b.append(b)
    vetor_c.append(a)
    vetor_c.append(b)
    
print(vetor_a)
print(vetor_b)
print(vetor_c)