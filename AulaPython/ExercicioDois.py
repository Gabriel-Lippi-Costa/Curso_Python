idade = int(input("Digite a idade da pessoa: "))

if (idade <= 2 and idade > 0):
    print("A pessoa é um bebê.")
elif (idade >= 2 and idade <= 4):
    print("A pessoa é uma criança de colo.")
elif (idade >= 4 and idade <= 13):
    print("A pessoa é uma criança.")
elif (idade >= 13 and idade <= 20):
    print("A pessoa é uma adolecente.")
elif (idade >= 20 and idade <= 65):
    print("A pessoa é uma adulta")
elif (idade >= 65 and idade <= 150):
    print("A pessoa é idosa.")
else:
    print("Valor inválido.")