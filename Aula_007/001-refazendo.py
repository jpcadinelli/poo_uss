class Transacao:
    def __init__(self):
        self.dataTransacao = ""
        self.qtde = 0
        self.produto = None

    def getDataTransacao(self):
        return self.dataTransacao

    def setDataTransacao(self, dataTransacao):
        self.dataTransacao = dataTransacao

    def getQtde(self):
        return self.qtde

    def setQtde(self, qtde):
        self.qtde = qtde

    def getProduto(self):
        return self.produto

    def setProduto(self, produto):
        self.produto = produto

class Compra(Transacao):
    def __init__(self):
        super().__init__()
        self.precoUnit = 0
        self.fornecedor = None

    def getPrecoUnit(self):
        return self.precoUnit

    def setPrecoUnit(self, precoUnit):
        self.precoUnit = precoUnit

    def getFornecedor(self):
        return self.fornecedor

    def setFornecedor(self, fornecedor):
        self.fornecedor = fornecedor

class Venda(Transacao):
    def __init__(self):
        super().__init__()
        self.cliente = None

    def getCliente(self):
        return self.cliente

    def setCliente(self, cliente):
        self.cliente = cliente

    def vender(self, produto, qtdeVendida):
        pass

class Produto():
    def __init__(self):
        self.nome = ""
        self.qtdeEstoque = 0
        self.precoUnit = 0
        self.estoqueMinimo = 0
        self.estoqueMaximo = 0
        self.historico = ""

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getQtdeEstoque(self):
        return self.qtdeEstoque

    def setQtdeEstoque(self, qtdeEstoque):
        self.qtdeEstoque = qtdeEstoque

    def getPrecoUnit(self):
        return self.precoUnit

    def setPrecoUnit(self, precoUnit):
        self.precoUnit = precoUnit

    def getEstoqueMinimo(self):
        return self.estoqueMinimo

    def setEstoqueMinimo(self, estoqueMinimo):
        self.estoqueMinimo = estoqueMinimo

    def getEstoqueMaximo(self):
        return self.estoqueMaximo

    def setEstoqueMaximo(self, estoqueMaximo):
        self.estoqueMaximo = estoqueMaximo

    def getHistorico(self):
        return self.historico

    def setHistorico(self, historico):
        self.historico = historico

    def debitarEstoque(self, quantidade):
        self.qtdeEstoque -= quantidade

    def creditarEstoque(self, quantidade):
        self.qtdeEstoque += quantidade

    def verificaEstoqueBaixo(self):
        if self.qtdeEstoque < self.estoqueMinimo:
            return True
        return False

    def verificaEstoqueInsuficiente(self, quantidade):
        if self.qtdeEstoque < quantidade:
            return True
        return False

    def verificaEstoqueExcedente(self, quantidade):
        if self.qtdeEstoque + quantidade >= self.estoqueMaximo:
            return True
        return False

    def calculaValorVenda(self, quantidade):
        return self.precoUnit * quantidade

    def vender(self, dataVenda, cliente, qtdeVendida):
        venda = Venda()
        venda.setCliente(cliente)
        venda.setDataTransacao(dataVenda)
        venda.setQtde(qtdeVendida)
        venda.setProduto(self)
        venda.vender(self, qtdeVendida)

class Pessoa:
    def __init__(self):
        self.nome = ""

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

class Fornecedor(Pessoa):
    def __init__(self):
        super().__init__()
        self.cnpj = ""

    def getCnpj(self):
        return self.cnpj

    def setCnpj(self, cnpj):
        self.cnpj = cnpj

class Cliente(Pessoa):
    def __init__(self):
        super().__init__()
        self.cpf = ""

    def getCpf(self):
        return self.cpf

    def setCpf(self, cpf):
        self.cpf = cpf