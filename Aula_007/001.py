class Produto:
    def __init__(self, nome, qtdeEstoque, precoUnit, estoqueMinimo, estoqueMaximo):
        self.nome = nome
        self.qtdeEstoque = qtdeEstoque
        self.precoUnit = precoUnit
        self.estoqueMinimo = estoqueMinimo
        self.estoqueMaximo = estoqueMaximo
        self.historico = []

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_precoUnit(self):
        return self.precoUnit

    def set_precoUnit(self, precoUnit):
        self.precoUnit = precoUnit

    def get_qtdeEstoque(self):
        return self.qtdeEstoque

    def set_qtdeEstoque(self, qtdeEstoque):
        self.qtdeEstoque = qtdeEstoque

    def get_estoqueMinimo(self):
        return self.estoqueMinimo

    def set_estoqueMinimo(self, estoqueMinimo):
        self.estoqueMinimo = estoqueMinimo

    def get_estoqueMaximo(self):
        return self.estoqueMaximo

    def set_estoqueMaximo(self, estoqueMaximo):
        self.estoqueMaximo = estoqueMaximo

    def get_historico(self):
        return self.historico

    def set_historico(self, historico):
        self.historico.append(historico)

    def registrarHistorico(self, transacao):
        self.historico = transacao

    def exibirHistorico(self):
        return self.historico

    def debitarEstoque(self, quantidade):
        self.qtdeEstoque -= quantidade

    def creditarEstoque(self, quantidade):
        self.qtdeEstoque += quantidade

    def verificarEstoqueBaixo(self):
        return self.qtdeEstoque < self.estoqueMinimo

    def verificarEstoqueInsuficiente(self, quantidade):
        return quantidade > self.qtdeEstoque

    def verificarEstoqueExcedente(self, quantidade):
        return (quantidade + self.qtdeEstoque) >= self.estoqueMaximo

    def calculaValorVenda(self, quantidade):
        return self.precoUnit * quantidade

    def vender(self, dataVenda, cliente, qtdeVendida):
        venda = Venda()
        if venda.vender(dataVenda, cliente, self, qtdeVendida):
            self.registrarHistorico(f"Venda do produto {self.get_nome()}")

    def comprar(self, dataCompra, fornecedor, qtdeCompra, precoUnit):
        compra = Compra()
        if compra.comprar(dataCompra, fornecedor, qtdeCompra, precoUnit, self):
            self.registrarHistorico(f"Compra do produto {self.get_nome()}")


class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def pessoa(self, nome):
        self.nome = nome


class Cliente(Pessoa):
    def __init__(self, cpf):
        Pessoa.__init__(self)
        self.cpf = cpf

    def get_cpf(self):
        return self.cpf

    def set_cpf(self, cpf):
        self.cpf = cpf

    def cliente(self, nome, cpf):
        self.pessoa(nome)
        self.cpf = cpf


class Fornecedor(Pessoa):
    def __init__(self, cnpj):
        Pessoa.__init__(self)
        self.cnpj = cnpj

    def get_cnpj(self):
        return self.cnpj

    def set_cnpj(self, cnpj):
        self.cnpj = cnpj

    def fornecedor(self, nome, cnpj):
        self.pessoa(nome)
        self.cnpj = cnpj


class Transacao():
    def __init__(self, dataTransacao, qtde):
        self.dataTransacao = dataTransacao
        self.qtde = qtde

    def get_dataTransacao(self):
        return self.dataTransacao

    def set_dataTransacao(self, dataTransacao):
        self.dataTransacao = dataTransacao


class Compra(Transacao):
    def __init__(self, preco):
        Transacao.__init__(self)
        self.preco = preco

    def get_preco(self):
        return self.preco

    def set_preco(self, preco):
        self.preco = preco

    def comprar(self, dataCompra, fornecedor, qtdeCompra, produto):
        if produto.verificarEstoqueExcedente(qtdeCompra):
            print("Ultrapassou a quantidade máxima")
            return False
        produto.creditarEstoque(qtdeCompra)
        return True


class Venda(Transacao):
    def __init__(self):
        Transacao.__init__(self)

    def vender(self, produto, qtdeVendida):
        if produto.verificarEstoqueInsuficiente(qtdeVendida):
            print("Estoque insuficiente")
            return False
        produto.debitarEstoque(qtdeVendida)
        print("O valor da venda é R$", produto.calculaValorVenda(qtdeVendida))
        if produto.verificarEstoqueBaixo():
            print("Estoque baixo")
        return True