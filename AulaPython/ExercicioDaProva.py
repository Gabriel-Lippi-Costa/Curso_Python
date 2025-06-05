gabarito = []
resposta_aluno = []
numeros_de_alunos = 0
matricula_aluno = []

for i in range(30):
    resposta = input(f"Digite a resposta da {i + 1} questão: ")
    gabarito.append(resposta)

numeros_de_alunos = int(input("Digite o número de alunos na turma: "))

for i in range(len(numeros_de_alunos)):
    resposta = input(f"Digite a resposta da questão {i + 1} questão: ")
    resposta_aluno.append(resposta)


acerto = 0
erro = 0

for i in range(len(gabarito)):
    if resposta_aluno[i] == gabarito[i]:
        acerto += 1
    else:
        erro += 1
    
for i in range(len(matricula_aluno)):
    print(f"Aluno matrícula: " + matricula_aluno[i] + ", Acertos: " + {acerto} + "Erros: " + {erro})