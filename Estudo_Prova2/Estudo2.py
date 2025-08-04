def info_numeros(numero1, numero2, numero3):
    lista = [numero1, numero2, numero3]

    maior_valor = max(lista)
    menor_valor = min(lista)
    media_valor = sum(lista) / len(lista)

    print(f"Maior valor: {maior_valor}")
    print(f"Menor valor: {menor_valor}")
    print(f"Média: {media_valor}")        

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um número: "))
numero3 = int(input("Digite um número: "))

info_numeros(numero1, numero2, numero3)