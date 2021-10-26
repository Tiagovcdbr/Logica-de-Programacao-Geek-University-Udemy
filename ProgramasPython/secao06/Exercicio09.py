#entradas
indice = float(input("Informe o índice de poluição: "))
#processamento
if indice >= 0.3 and indice < 0.4:
    print("Atenção: Indústrias do 1o grupo devem suspender as atividades.")
elif indice >= 0.4 and indice < 0.5:
    print("Atenção: Indústrias do 1o e 2o grupo devem suspender as atividades.")
elif indice >= 0.5:
    print("Atenção: Todos os grupos devem suspender as atividades.")
