def quicksort(lista):
    if len(lista) < 2:
        return lista
    
    pivo = lista.pop(0)
    menores = [i for i in lista if i <= pivo]
    maiores = [i for i in lista if i > pivo]
    return quicksort(menores) + [pivo] + quicksort(maiores)

print(quicksort([33, 15, 10]))