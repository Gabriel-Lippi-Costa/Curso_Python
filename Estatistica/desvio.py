import statistics

conjunto_valores = [2, 4, 6]
lista_desvios = []

def calcular_media_conjunto_valores(conjunto_valores):
    media_conjunto_valores = statistics.mean(conjunto_valores)
    return media_conjunto_valores 

def calcular_desvio(conjunto_valores, media_conjunto_valores):
    soma = 0
    for valor in conjunto_valores:
        desvio = valor - media_conjunto_valores
        soma += desvio
        lista_desvios.append(desvio)
    
    return soma, lista_desvios

media_conjunto_valores = calcular_media_conjunto_valores(conjunto_valores)

resultado_desvio, lista_desvios = calcular_desvio(conjunto_valores, media_conjunto_valores)

print(f"Essa é a média do seu conjunto de valores: {media_conjunto_valores}\n")
print(f"Esse é o seu total de desvios: {resultado_desvio}")
print(f"Essa é a sua lista de desvios: {lista_desvios}")