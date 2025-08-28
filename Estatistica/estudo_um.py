import math

lista_numeros_observacoes = [18, 22, 20, 19, 21, 20, 18, 22, 21, 19, 20, 19, 22, 18, 21, 23, 25, 28, 30, 35]

def calcular_classes(numero_observacoes):
    resultado = math.sqrt(numero_observacoes)
    if isinstance(resultado, float):
        return arredonda_classes(resultado)
    else:
        print(f"Esse é o seu número de classes: {resultado}")
        return resultado

def arredonda_classes(resultado):
    print("Agora vamos arredondar a classe.")
    classe_arredondada = round(resultado)
    print(f"Esse é o seu número de classes: {classe_arredondada}")
    return classe_arredondada
    
def calcular_amplitude_distribuicao(lista_numeros_observacoes):
    limite_inferior = min(lista_numeros_observacoes)
    limite_superior = max(lista_numeros_observacoes)

    R = limite_superior - limite_inferior

    print(f"Esse é a sua amplitude de distribuição: {R}")

    return R

def calcular_amplitude_classes(R, numeros_classes):
    resultado = R / numeros_classes
    print(f"Essa é a sua amplitude de classes: {resultado}")  
    return resultado   

numeros_observacoes = len(lista_numeros_observacoes)
numeros_classes = calcular_classes(numeros_observacoes)
R = calcular_amplitude_distribuicao(lista_numeros_observacoes)
H = calcular_amplitude_classes(R, numeros_classes)