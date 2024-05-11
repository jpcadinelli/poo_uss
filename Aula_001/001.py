class Aluno:

    def __init__(self):
        self.nome = ''
        self.matricula = 0
        self.endereco = ''
        self.telefone = ''
        self.nota1 = 0.0
        self.nota2 = 0.0

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
    
    def setNota1(self, nota1):
        self.nota1 = nota1

    def getNota1(self):
        return self.nota1
    
    def setNota2(self, nota2):
        self.nota2 = nota2

    def getNota2(self):
        return self.nota2
    
    def calcularMedia(self):
        media = (self.nota1 + self.nota2) / 2
        return media
    
    def getStatus(self):
        if self.calcularMedia() >= 7:
            status = 'Aprovado'
        elif self.calcularMedia() >= 4:
            status = 'Prova Final'
        else:
            status = 'Reprovado'
        return status
    
aluno = Aluno()
aluno.setNome('João')
print(aluno.getNome())
aluno.setMatricula(2024001)
print(aluno.getMatricula())
aluno.setEndereco('rua Professor Marcão, 10, bairro Vasco da Gama, Juiz de Fora - MG')
print(aluno.getEndereco())
aluno.setTelefone('(99) 99999-9999')
print(aluno.getTelefone())
aluno.setNota1(7)
print(aluno.getNota1())
aluno.setNota2(9)
print(aluno.getNota2())
print(aluno.getStatus())

# aluno2 = Aluno()
# aluno2.setNome('Maria')
# print(aluno2.getNome())