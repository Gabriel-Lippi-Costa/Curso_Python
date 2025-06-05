import re

#Exercício 0
lista_numeros = []

resultado_media = 0

contagem = int(input("Digite quantos número você deseja colocar: "))

for i in range(contagem):
    numero_media = float(input("Digite um número: "))
    lista_numeros.append(numero_media)
    resultado_media += numero_media

tamanho_lista = len(lista_numeros)

media_aritmetica = resultado_media / tamanho_lista

print(media_aritmetica)

#Exercício 1
num = int(input("Digite um número: "))

if (num % 2 == 0):
    print(f"O número {num} é par!") 
else:
    print(f"O número {num} é ímpar!")

# Exercício 2
celsius = float(input("Digite a sua temperatura em Celsius: "))

conversao = (celsius * 1.8) + 32

print(f"A conversão da sua temperatura ficou: {conversao}F.")

#Exercício 3
lista = []

passo = int(input("Digite quantas palavras você vai por na lista: "))
for i in range(passo):
    palavra = input("Digite alguma palavra: ")
    lista.append(palavra)

contador = int(input("Digite quantas vezes vai querer fazer a busca: "))  
i = 0     
for i in range(contador):
    palavra_verificar = input("Digite alguma palavra: ")
    if palavra_verificar in lista:
        print(f"Essa palavra está na lista. Contador {i + 1}º.")
    else:
        print("Não está na lista.")

#Exercício 4
lista_numeros = []

c = int(input("Digite quantas vezes você irá colocar números na lista: "))

for i in range(c):
    num = float(input("Digite um número: "))
    lista_numeros.append(num)

maior = max(lista_numeros)
print(f"O maior número da lista é {maior}.")

#Exercício 5
numero_primo = int(input("Digite um número para descobrir se é primo: "))
primo = True

if numero_primo <= 1:
    print(f"O número {numero_primo} não é primo!")
    primo = False
elif numero_primo == 2:
    print(f"O número 2 é primo!")
else:
    for i in range(2, numero_primo):
        if numero_primo % i == 0:
            primo = False  
            break
        
if primo:
    print("É primo!")
else:
    print("Não é primo!")

#Exercício 6            
capital = float(input("Digite em apenas o valor do capital: "))

montante = capital * ((1 + 0.1)**12)

print(f"O seu montante foi de R${montante:.2f}")

Exercício 7
texto = input("Digite qualquer palavra: ")

invertido = texto[::-1]

print(f"O seu texto invertido ficou como: {invertido}")

#Exercício 8
texto_invertido = input("Digite qualquer palavra: ")

invercao = texto_invertido[::-1]

if texto_invertido == invercao:
    print(f"A sua palavra '{texto_invertido}' ela é um palíndromo.")
else:
    print(f"A sua palavra '{texto_invertido}' não é um palíndromo")

Exercício 9
texto_subistituir = input("Digite qualquer palavra: ")

nova_frase = re.sub('[aeiou]', '*', texto_subistituir)

print(nova_frase)

#Exercício 10
#Letra C