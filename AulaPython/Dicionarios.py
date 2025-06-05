Pessoa = {
    'nome': "Marina",
    'cargo': "Analista de Dados",
    'idade': 27,
    'ativo': True
}

print(Pessoa['nome'])
print(Pessoa['cargo'])

temEmail = True

for i in Pessoa:
    if 'email' in Pessoa:
        temEmail = True
    else:
        naoTem = False
        

if temEmail == True:
    print("Tem e-mail.")
else: 
    print("Não tem e-mail.")

print(Pessoa.get('email', "Não informado!"))

