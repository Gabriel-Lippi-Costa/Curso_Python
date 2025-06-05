Carrinho = [
    {'nome': 'Caneta', 'quantidade': 2, 'preco': 1.50},
    {'nome': 'Caderno', 'quantidade': 1, 'preco': 12.90},
    {'nome': 'Mochila', 'quantidade': 1, 'preco': 1.50}
]

for produto in Carrinho:
    print("Produto:", produto['nome'])

for produto in Carrinho:
    total_produto = produto['quantidade'] * produto['preco']
    print(total_produto)

soma = 0
for produto in Carrinho:
    soma += produto['quantidade'] * produto['preco']

print(soma)

Carrinho.append({'nome': 'Lápis', 'quantidade': 5, 'preco': 0.90})

print(Carrinho)

Carrinho[1].update({'quantidade': 2})
print(Carrinho)

