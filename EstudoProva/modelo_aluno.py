class Aluno:
    def __init__(self, nome, matricula, curso, senha_portal):
        self.nome = nome
        self.matricula = matricula
        self._curso = curso
        self.__senha_portal = senha_portal

    def mostrar_dados_simples(self):
        print(f"Nome: {self.nome}")
        print(f"Matrícula: {self.matricula}")

    @property
    def mostrar_curso(self):
        return self._curso
    
    @property
    def mostrar_senha(self):
        return self.__senha_portal

class AlunoGraduacao(Aluno):
    def __init__(self, nome, matricula, curso, senha_portal, semestre):
        super().__init__(nome, matricula, curso, senha_portal)
        self.semestre = semestre

    def mostrar_dados(self):
        super().mostrar_dados_simples()
        print(f"Semestre: {self.semestre}")