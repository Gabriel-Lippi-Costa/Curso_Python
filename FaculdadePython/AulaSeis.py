def calcula_fatorial(fatorial):
    while fatorial == 1:
        return fatorial * calcula_fatorial(fatorial - 1)

fatorial = int(input("Digite um número para descobrir o seu fatorial: "))

print(calcula_fatorial(fatorial))