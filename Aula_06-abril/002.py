class Pessoa:
    
    def __init__(self):
        self.nome = ""
        self.endereco = ""
    
    def setNome(self, nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome
    
    def setEndereco(self, endereco):
        self.endereco = endereco
    
    def getEndereco(self):
        return self.endereco

class PessoaFisica(Pessoa):
    
    def __init__(self):
        Pessoa.__init__(self)
        self.cpf = ""
    
    def setCpf(self, cpf):
        self.cpf = cpf

    def getCpf(self):
        return self.cpf

class PessoaJuridica(Pessoa):
    
    def __init__(self):
        Pessoa.__init__(self)
        self.cnpj = ""
    
    def setCnpj(self, cnpj):
        self.cnpj = cnpj
    
    def getCnpj(self):
        return self.cnpj