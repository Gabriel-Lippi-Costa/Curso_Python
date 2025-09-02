conjunto_valores = [1,22,2,5,4,8]

def calcular_aplitude(conjunto_valores):
    resultado_amplitude = max(conjunto_valores) - min(conjunto_valores)
    print(resultado_amplitude)
    return resultado_amplitude

resultado_amplitude = calcular_aplitude(conjunto_valores)

print(f"Essa é a amplitude do seu conjunto de valores: {resultado_amplitude}")