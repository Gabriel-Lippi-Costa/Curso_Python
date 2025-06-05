Pessoa = {
    'nome': "Marina",
    'cargo': "Analista de Dados",
    'idade': 27,
    'ativo': True
}

Pessoa["idade"] = 29

Pessoa.update({'salario': 8500})
print(Pessoa)
Pessoa.update({'e-mail': "marina@empresa.com"})
print(Pessoa)
del Pessoa['ativo']
print(Pessoa)

for chave in Pessoa.values():
    print(chave)

for chave, valor in Pessoa.items():
    print(f"{chave} ({type(valor)._name_}): {valor}")