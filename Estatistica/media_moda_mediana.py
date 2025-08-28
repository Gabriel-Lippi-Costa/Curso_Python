import statistics

lista_valores = [86, 86, 96, 82, 98, 98, 98, 100]

def calcular_media(lista_valores):
    resultado = statistics.mean(lista_valores)

    return resultado

def calcular_mediana(lista_valores):
    resultado = statistics.median(lista_valores)

    return resultado

def calcular_moda(lista_valores):
    try:
        resultado = statistics.mode(lista_valores)
    except statistics.StatisticsError:
        resultado = statistics.multimode(lista_valores)

    return resultado

resultado_media = calcular_media(lista_valores)
resultado_mediana = calcular_mediana(lista_valores)
resultado_moda = calcular_moda(lista_valores)

print(f"Essa foi a sua média: {resultado_media}")
print(f"Essa foi a sua mediana: {resultado_mediana}")
print(f"Essa foi a sua moda: {resultado_moda}")