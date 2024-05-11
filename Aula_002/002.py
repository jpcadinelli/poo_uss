# Classe ContaBancaria:

# Atributos: titular, numero_conta, saldo
# Métodos: depositar, sacar
# •	depositar(valor): adiciona o valor ao saldo da conta.
# •	sacar(valor): subtrai o valor do saldo da conta, se houver saldo suficiente.

class ContaBancaria:

    def __init__(self):
        self.titular = ""
        self.numero_conta = 0
        self.saldo = 0.00
        self.estado = "ativa"
    
    def getTitular(self):
        return self.titular
    
    def setTitular(self, titular):
        self.titular = titular
    
    def getNumeroConta(self):
        return self.numero_conta
    
    def setNumeroConta(self, numeroConta):
        self.numero_conta = numeroConta
    
    def getSaldo(self):
        return self.saldo
    
    def setSaldo(self, saldo):
        if self.estado == "ativa":
            if saldo >= 0:
                self.saldo = saldo

    def getEstado(self):
        return self.estado
    
    def setEstado(self, estado):
        if estado == "ativa" or estado == "inativa":
            self.estado = estado    

    def depositar(self, valor):
        if self.estado == "ativa":
            if valor > 0:
                self.saldo += valor
    
    def sacar(self, valor):
        if self.estado == "ativa":
            if valor > 0 and valor <= self.saldo:
                self.saldo -= valor

    def ativar(self):
        self.estado = "ativa"

    def inativar(self):
        self.estado = "inativa"

conta = ContaBancaria()
conta.setSaldo(500)
conta.inativar()
print(conta.getSaldo())
conta.depositar(100)
print(conta.getSaldo())
conta.ativar()
conta.sacar(30)
print(conta.getSaldo())