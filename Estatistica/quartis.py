import statistics

lista_valores = [86, 86, 96, 82, 98, 98, 98, 100]

def calcular_quartis(lista_valores):
    quartis = statistics.quantiles(lista_valores, n=quantidade_quartis)

    return quartis

quantidade_quartis = int(input("Digite a quantidade de quartis para sua \nlista de valores:"))

resultado_quartis = calcular_quartis(lista_valores)

print(f"Todos os quartis: {resultado_quartis}")