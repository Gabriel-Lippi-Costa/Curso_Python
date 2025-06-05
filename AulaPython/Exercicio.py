gabarito = []
respostas_alunos = []
matriculas = []

for i in range(30):
    resposta = input(f"Digite a resposta da {i + 1}ª questão do gabarito: ")
    gabarito.append(resposta)  

numeros_de_alunos = int(input("Digite o número de alunos na turma: "))

for i in range(numeros_de_alunos):
    print(f"Aluno {i + 1}")
    matricula = input("Digite a matrícula do aluno: ")
    matriculas.append(matricula)

    respostas = []
    for j in range(30):
        resposta = input(f"Resposta da questão {j + 1}: ")
        respostas.append(resposta)
    respostas_alunos.append(respostas)

for i in range(numeros_de_alunos):
    acertos = 0
    erros = 0
    for j in range(30):
        if respostas_alunos[i][j] == gabarito[j]:
            acertos += 1
        else:
            erros += 1
    print(f"Aluno matrícula: {matriculas[i]} - Acertos: {acertos} - Erros: {erros}")
