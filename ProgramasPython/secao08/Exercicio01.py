#variáveis
vetor = [] #lista vazia
pares = [] #lista vazia
for n in range(1, 6):
    vetor.append(n)
    if n % 2 == 0:
        pares.append(n)
for p in pares:
    print(p)
