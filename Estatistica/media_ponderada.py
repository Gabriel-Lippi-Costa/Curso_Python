conjunto_valores = [86, 96, 82, 98, 100]
conjunto_pesos = [0.50, 0.15, 0.20, 0.10, 0.05]

def calcular_media_ponderada(conjunto_valores, conjunto_pesos):

    soma_ponderada = 0
    soma_peso = 0

    for valor, peso in zip(conjunto_valores, conjunto_pesos):
        soma_ponderada += valor * peso
        soma_peso += peso

    resultado = soma_ponderada / soma_peso

    return resultado       

resultado = calcular_media_ponderada(conjunto_valores, conjunto_pesos)

print(f"Essa foi a média ponderada: {resultado}")