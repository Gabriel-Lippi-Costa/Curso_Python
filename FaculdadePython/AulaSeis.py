'''
def calcula_fatorial(fatorial):
    if fatorial == 1:
        return 1
    else:
        return fatorial * calcula_fatorial(fatorial - 1)

fatorial = int(input("Digite um número para descobrir o seu fatorial: "))

print(calcula_fatorial(fatorial))


def calcula_numeros(numero):
    if numero == 1:
        return 1
    else:
        return numero + calcula_numeros(numero - 1)

numero = int(input("Digite um número para descobrir a soma dele: "))

print(calcula_numeros(numero))


def calcula_fibonacci(fibonacci):
    if fibonacci < 2:
        return fibonacci
    else:
        return calcula_fibonacci(fibonacci - 1) + calcula_fibonacci(fibonacci - 2)

fibonacci = int(input("Digite um número para descobrir a sequênica de Fibonacci: "))

print(calcula_fibonacci(fibonacci))


def calcula_potencia(base, expoente):
    if expoente == 0:
        return 1
    else:
        return base * calcula_potencia(base, expoente - 1)

base = int(input("Digite um número para a sua base: "))
expoente = int(input("Digite um número para o seu expoente: "))

print(calcula_potencia(base, expoente))


def inverte_palavra(palavra):
    if len(palavra) < 2:
        return palavra
    else:
        return palavra[-1] + inverte_palavra(palavra[:-1])

palavra = input("Digite uma palavra para eu inverter: ")

print(inverte_palavra(palavra))
'''