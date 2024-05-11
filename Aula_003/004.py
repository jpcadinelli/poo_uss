# Classe Funcionario:
# Atributos: nome, cargo, salario, departamento
# Métodos: receber_aumento, mudar_departamento, exibir_dados
#     • receber_aumento(percentual): Aplica um aumento de percentual ao salario.
#     • mudar_departamento(novo_departamento): Altera o departamento para o novo_departamento.
#     • exibir_dados(): Exibe os dados do funcionário, incluindo nome, cargo, salário e departamento.

class Funcionario:

    def __init__(self):
        self.nome = ""
        self.cargo = ""
        self.salario = 0
        self.departamento = ""
    
    def getNome(self):
        return self.nome
    
    def setNome(self, nome):
        self.nome = nome
    
    def getCargo(self):
        return self.cargo
    
    def setCargo(self, cargo):
        self.cargo = cargo
    
    def getSalario(self):
        return self.salario
    
    def setSalario(self, salario):
        self.salario = salario
    
    def getDepartamento(self):
        return self.departamento
    
    def setDepartamento(self, departamento):
        self.departamento = departamento

    def receberAumento(self, percentual):
        if percentual > 0:
            self.salario += self.salario * (percentual / 100)

    def mudarDepartamento(self, novo_departamento):
        self.departamento = novo_departamento

    def exibirDados(self):
        print("DADOS DO FUNCIOÁRIO")
        print("*******************")
        print("Nome: ", self.nome)
        print("Cargo: ", self.cargo)
        print("Salário: R$", self.salario)
        print("Departamento: ", self.departamento)


funcionario = Funcionario()
funcionario.setSalario(1000)
funcionario.receberAumento(10)
# print(funcionario.getSalario())
funcionario.mudarDepartamento("Informatica")
# print(funcionario.getDepartamento())
funcionario.setNome("Luann")
funcionario.setCargo("Estagiário")
funcionario.exibirDados()