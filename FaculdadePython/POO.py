'''
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá eu sou a {self.nome} e tenho {self.idade} anos.")

pessoa1 = Pessoa("Maria", 30)
pessoa1.apresentar()
'''

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar_valor(self, saldo):
        self.saldo += saldo

    def sacar(self, valor):
        if self.saldo <= 0:
            print("Você não tem saldo na conta!")
        else:
            self.saldo -= valor
            print(f"Saldo atual: {self.saldo}")
    
    def mostrar_saldo(self):
        print(f"Esse é o seu saldo: {self.saldo}")

pessoa1 = ContaBancaria("Gabriel", 1000)
pessoa1.depositar_valor(500)
pessoa1.sacar(500)
pessoa1.mostrar_saldo()
