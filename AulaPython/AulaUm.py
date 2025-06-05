#Exercício 1
ano = int(input("Digite o seu ano no formato (YYYY): "))

if ano % 4 == 0:  # Etapa 1
    if ano % 100 == 0:  # Etapa 2
        if ano % 400 == 0:  # Etapa 3
            print("O ano é bissexto.")  # Etapa 4
        else:
            print("O ano não é bissexto.")  # Etapa 5
    else:
        print("O ano é bissexto.")  # Etapa 4
else:
    print("O ano não é bissexto.")  # Etapa 5