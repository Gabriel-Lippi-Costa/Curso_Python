caracter = input("Digite qualquer caractere mas apenas um: ")

tipo = ord(caracter)

if (tipo >= 65 and tipo <= 90):
    print("É uma letra maiúscula.")
elif (tipo >= 97 and tipo <= 122):
    print("É uma letra minúscula.")
elif (tipo >= 48 and tipo <= 57):
    print("É um algarismo decimal")
else:
    print("Caracter especial.")