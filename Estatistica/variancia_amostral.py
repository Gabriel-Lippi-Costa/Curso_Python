import statistics
import math

conjunto_valores = [4, 7, 6, 7, 9, 5, 8, 10, 9, 8, 7, 10]
lista_desvios = []
lista_desvios_quadrados = []

def calcular_media_conjunto_valores(conjunto_valores):
    media_conjunto_valores = statistics.mean(conjunto_valores)
    return media_conjunto_valores

def calcular_variancia_amostral(conjunto_valores, media_conjunto_valores):
    soma_desvio = 0
    soma_desvio_quadrado = 0

    for valor in conjunto_valores:
        desvio = valor - media_conjunto_valores
        soma_desvio += desvio
        desvio_quadrado = (valor - media_conjunto_valores) ** 2
        soma_desvio_quadrado += desvio ** 2
        lista_desvios.append(desvio)
        lista_desvios_quadrados.append(desvio_quadrado)

    return soma_desvio, soma_desvio_quadrado, lista_desvios, lista_desvios_quadrados


resultado_media_conjunto = calcular_media_conjunto_valores(conjunto_valores)

resultado_desvio, resultado_desvio_quadrado, lista_desvios, lista_desvios_quadrados = calcular_variancia_amostral(conjunto_valores, resultado_media_conjunto)

print(f"Essa é a sua média do conjunto: {resultado_media_conjunto}\n")
print(f"Essa é a sua lista de desvios: {lista_desvios}")
print(f"Esse é o seu total de desvios: {resultado_desvio}\n")
print(f"Esse é o seu total do desvios ao quadrado: {resultado_desvio_quadrado}")
print(f"Essa é a sua lista de desvios ao quadrado: {lista_desvios_quadrados}")
print(f"Essa é a sua variância amostral: {resultado_desvio_quadrado / len(conjunto_valores)}")