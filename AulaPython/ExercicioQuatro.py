tipo_brinquedo = input("O seu brinquedo usa bateria, pilha ou bateria recarregável?")

preco_brinquedo = float(input("Digite o valor do seu brinquedo:"))

if (tipo_brinquedo == "Bateria" and preco_brinquedo >= 1000):
    print("Você ganhou um desconto de 10%.")
    preco_brinquedo = preco_brinquedo - (preco_brinquedo * 0.1)
    print(f"Ficou no total: R${preco_brinquedo:.2f}")

elif (tipo_brinquedo == "Pilha" and preco_brinquedo >= 100):
    print("Você ganhou um desconto de 5%.")
    preco_brinquedo = preco_brinquedo - (preco_brinquedo * 0.05)
    print(f"Ficou no total: R${preco_brinquedo:.2f}.")

elif (tipo_brinquedo == "Bateria recarregável" and preco_brinquedo >= 500):
    print("Você ganhou um desconto de 10%.")
    preco_brinquedo = preco_brinquedo - (preco_brinquedo * 0.1)
    print(f"Ficou no total: R${preco_brinquedo:.2f}")

else:
    print(f"Esse é o tipo do seu brinquedo {tipo_brinquedo} e esse é o preço dele R${preco_brinquedo:.2f}")
