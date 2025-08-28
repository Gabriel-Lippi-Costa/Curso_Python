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
    print(f"Essa é a sua amplitude de classes: {resultado}\n")  
    return resultado   

def definir_classes(limite_inferior, numeros_classes, H):
    classes = []

    for i in range(numeros_classes):
        if i == 0:
            li = limite_inferior
        else:
            li = classes[i-1][1] + 0.1

        ls = li + H
        classes.append((round(li,1), round(ls,1)))
    
    return classes

def contagem_observacoes(lista_numeros_observacoes, classes):
    frequencia = {}

    for li, ls in classes:
        count = sum(1 for x in lista_numeros_observacoes if li <= x <= ls)
        frequencia[(li, ls)] = count

    return frequencia

numeros_observacoes = len(lista_numeros_observacoes)
print("")
print("Informações iniciais:")
numeros_classes = calcular_classes(numeros_observacoes)
R = calcular_amplitude_distribuicao(lista_numeros_observacoes)
H = calcular_amplitude_classes(R, numeros_classes)

limite_inferior = min(lista_numeros_observacoes)
classes = definir_classes(limite_inferior, numeros_classes, H)
frequencia = contagem_observacoes(lista_numeros_observacoes, classes)

print("Classes definidas:")
for idx, (li, ls) in enumerate(classes, start=1):
    print(f"Classe: {idx}: {li} - {ls}")

print("")

print("Contagem:")
for (li, ls), count in frequencia.items():
    print(f"Classe: {li} - {ls}: {count}")