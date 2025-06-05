notas_alunos = []

def adicionar_nota():
    nome = input("Nome do aluno: ")
    try:
        nota = float(input("Nota do aluno: "))
        if 0 <= nota <= 10:
            notas_alunos[nome] = nota
            print(f"Nota {nota} adicionada para {nome}.")
        else:
            print("A nota deve estar entre 0 e 10.")
    except ValueError:
        print("Por favor, digite um valor numérico válido.")

def remover_nota():
    listar_notas()
    if not notas_alunos:
        return
    nome = input("Nome do aluno para remover a nota: ")
    if nome in notas_alunos:
        del notas_alunos[nome]
        print(f"Nota de {nome} removida com sucesso!")
    else:
        print("Aluno não encontrado.")

def calcular_media():
    if not notas_alunos:
        print("Nenhuma nota cadastrada.")
        return
    media = sum(notas_alunos.values()) / len(notas_alunos)
    print(f"Média das notas: {media:.2f}")

def listar_notas():
    if not notas_alunos:
        print("Nenhum aluno cadastrado.")
        return
    for i, (nome, nota) in enumerate(notas_alunos.items(), 1):
        print(f"{i}. {nome}: {nota}")

# Menu interativo
while True:
    print("\n1. Adicionar Nota")
    print("2. Remover Nota")
    print("3. Calcular Média")
    print("4. Listar Notas")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        adicionar_nota()
    elif opcao == "2":
        remover_nota()
    elif opcao == "3":
        calcular_media()
    elif opcao == "4":
        listar_notas()
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida, tente novamente.")