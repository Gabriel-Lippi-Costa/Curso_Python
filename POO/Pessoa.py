class Funcionario:
    def __init__(self, nome, salario, senha):
        self.nome = nome
        self._salario = salario
        self.__senha = senha

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, novo_salario):
        if novo_salario >= 1000:
            self._salario = novo_salario
        else:
            print("Salário inválido. Deve ser maior ou igual que 1000")

    @property
    def senha(self):
        return self.__senha

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: {self._salario}")
        print(f"Senha: {self.__senha}")


class Gerente(Funcionario):
    def __init__(self, nome, salario, senha, departamento):
        super().__init__(nome, salario, senha)
        self.departamento = departamento

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: {self._salario}")
        print(f"Senha: {self.senha}")
        print(f"Departamento: {self.departamento}")

# p = Funcionario("Gabriel", 1500, "GabrielSenha")
# p.mostrar_dados()

#g = Gerente("Ana", 6500, "AnaSenha", "Professora")
#g.mostrar_dados()

