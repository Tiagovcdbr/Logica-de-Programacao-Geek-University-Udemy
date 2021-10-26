#entradas
num1 = int(input("Informe o número 1: "))
num2 = int(input("Informe o número 2: "))
num3 = int(input("Informe o número 3: "))
num4 = int(input("Informe o número 4: "))
#processamento
q1 = num1 * num1
q2 = num2 * num2
q3 = num3 * num3
q4 = num4 * num4

if q3 >= 1000:
    print(q3)
else:
    print("Num1: {0}, Quadrado: {1}".format(num1, q1))
    print("Num2: {0}, Quadrado: {1}".format(num2, q2))
    print("Num3: {0}, Quadrado: {1}".format(num3, q3))
    print("Num4: {0}, Quadrado: {1}".format(num4, q4))
