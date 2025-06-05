num = int(input("Digite um número para descobrir se é primo: "))

primo = True

if num <= 1:
    print("O seu número não é primo.")
else:
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break

if primo:
    print("É primo.")
else:
    print("Não é primo.")