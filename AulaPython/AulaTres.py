#Exercício 3

n1 = int(input("Digite o valor do primeiro número: "))
n2 = int(input("Digite o valor do segundo número: "))

while (n1 != n2):
    n1 = n1 + 1
    if (n1 == n2):
        break
    print(n1)