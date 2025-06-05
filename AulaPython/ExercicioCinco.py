unidades_consumidas = int(input("Digite o valor da unidades consumidas: "))

if (unidades_consumidas > 0 and unidades_consumidas <= 100):
    preco = unidades_consumidas * 0.50
    print(f"Ficou no total: R${preco:.2f}")

elif (unidades_consumidas > 100 and unidades_consumidas <= 200):
    preco = 50 + unidades_consumidas
    print(f"Ficou no total: R${preco:.2f}")

elif (unidades_consumidas > 200 and unidades_consumidas <= 300):
    preco = 150 + unidades_consumidas
    print(f"Ficou no total: R${preco:.2f}")

elif (unidades_consumidas > 300):
    preco = 300 + (unidades_consumidas * 2)
    print(f"Ficou no total: {preco:.2f}")

else:
    print("Valor inválido!")