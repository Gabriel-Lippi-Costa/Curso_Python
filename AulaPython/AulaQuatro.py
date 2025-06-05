tarefas = []

def adicionar_tarefa():
    nome = input("Nome da tarefa: ")
    tarefas.append({"nome": nome, "concluida": False})
    print(f"Tarefa '{nome}' adicionada com sucesso!")

def remover_tarefa():
    listar_tarefas()
    if not tarefas:
        return
    nome = input("Nome da tarefa para remover: ")
    for tarefa in tarefas:
        if tarefa["nome"] == nome:
            tarefas.remove(tarefa)
            print(f"Tarefa '{nome}' removida com sucesso!")
            return
    print("Tarefa não encontrada.")

def marcar_concluida():
    listar_tarefas()
    if not tarefas:
        return
    nome = input("Nome da tarefa para marcar como concluída: ")
    for tarefa in tarefas:
        if tarefa["nome"] == nome:
            tarefa["concluida"] = True
            print(f"Tarefa '{nome}' marcada como concluída!")
            return
    print("Tarefa não encontrada.")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    for i, tarefa in enumerate(tarefas, 1):
        status = "[Concluída]" if tarefa["concluida"] else "[Pendente]"
        print(f"{i}. {tarefa['nome']} {status}")

# Menu interativo
while True:
    print("\n1. Adicionar Tarefa")
    print("2. Remover Tarefa")
    print("3. Marcar Tarefa como Concluída")
    print("4. Listar Tarefas")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        remover_tarefa()
    elif opcao == "3":
        marcar_concluida()
    elif opcao == "4":
        listar_tarefas()
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida, tente novamente.")