class Aluno:

    def __init__(self):
        self.nome = ''
        self.matricula = 0
        self.endereco = ''
        self.telefone = ''

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome
    
    def setMatricula(self, matricula):
        self.matricula = matricula

    def getMatricula(self):
        return self.matricula
    
    def setEndereco(self, endereco):
        self.endereco = endereco

    def getEndereco(self):
        return self.endereco
    
    def setTelefone(self, telefone):
        self.telefone = telefone

    def getTelefone(self):
        return self.telefone
    
aluno = Aluno()
aluno.setNome('João')
print(aluno.getNome())
aluno.setMatricula(2024001)
print(aluno.getMatricula())
aluno.setEndereco('rua Professor Marcão, 10, bairro Vasco da Gama, Juiz de Fora - MG')
print(aluno.getEndereco())
aluno.setTelefone('(99) 99999-9999')
print(aluno.getTelefone())

# aluno2 = Aluno()
# aluno2.setNome('Maria')
# print(aluno2.getNome())