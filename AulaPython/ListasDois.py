lista_compras = []

def add_compra():
    produto = input("Adicione um item: ")
    lista_compras.append(produto)
    print(f"Produto {produto} adicionado com sucesso!")

def listar_compras():
    if not lista_compras:
        print("Nenhum produto na lista.")
        return
    for i, produto in enumerate(lista_compras, 1):#usa a função enumerate() para percorrer a lista, atribuindo um número sequencial a cada elemento.
        print(f"{i}. {produto}") 

def limpar_lista():
    lista_compras.clear()

def remover_produto():
    listar_compras()
    if not lista_compras:
        return
    try: #O try serve para tentar executar um bloco de código e capturar erros, caso ocorram. Aqui, estamos tentando converter um número digitado pelo usuário em um índice da lista.
        indice = int(input("Digite o número da compra que deseja remover: ")) - 1
        if 0 <= indice < len(lista_compras):
            removido = lista_compras.pop(indice)
            print(f"Produto {removido} removido com sucesso!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")

# Menu interativo
while True:
    print("\n1. Adicionar Produto")
    print("2. Listar Compras")
    print("3. Limpar Lista")
    print("4. Remover Produto")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        add_compra()
    elif opcao == "2":
        listar_compras()
    elif opcao == "3":
        limpar_lista()
    elif opcao == "4":
        remover_produto()
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida, tente novamente.")
