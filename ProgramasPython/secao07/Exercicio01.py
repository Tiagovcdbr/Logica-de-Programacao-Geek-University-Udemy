#variáveis
maior = 0
#entrada
n = int(input("Informe um número: "))
while n != 0:
    if n > maior:
        maior = n
    n = int(input("Informe um número: "))
print("O maior número é {0}".format(maior))
