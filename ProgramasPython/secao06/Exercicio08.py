#entrada
numero = int(input("Informe um número: "))
#processamento
if numero % 2 == 0:
    if numero > 0:
        print("O número {0} é par e positivo".format(numero))
    else:
        print("O número {0} é par e negativo".format(numero))
else:
    if numero > 0:
        print("O número {0} é ímpar e positivo".format(numero))
    else:
        print("O número {0} é ímpar e negativo".format(numero))
