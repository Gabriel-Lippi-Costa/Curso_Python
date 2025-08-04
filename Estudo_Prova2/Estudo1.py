def deixar_maiuscula(nome_completo):
    return nome_completo.upper()

def deixar_invertido(nome_completo):
    return nome_completo[::-1]

def contar_vogais(nome_completo):
    lista_vogais = ["a", "e", "i", "o", "u"]

    contador_vogais = 0
    for letra in nome_completo.lower():
        if letra in lista_vogais:
            contador_vogais += 1

    return contador_vogais

nome_completo = "Gabriel Lippi da Costa"

print(f"Seu nome completo maiúsculo: {deixar_maiuscula(nome_completo)}")
print(f"Seu nome completo invertido: {deixar_invertido(nome_completo)}")
print(f"Quantidade de vogais no seu nome completo: {contar_vogais(nome_completo)}")