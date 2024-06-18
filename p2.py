class Pais:
    def __init__(self, pais):
        self.pais = pais

    def get_pais(self):
        return self.pais

    def set_pais(self, pais):
        self.pais = pais


class Estado:
    def __init__(self, estado, pais):
        self.estado = estado
        self.pais = pais

    def get_estado(self):
        return self.estado

    def set_estado(self, estado):
        self.estado = estado

    def get_pais(self):
        return self.pais

    def set_pais(self, pais):
        self.pais = pais


class Cidade:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def get_cidade(self):
        return self.cidade

    def set_cidade(self, cidade):
        self.cidade = cidade

    def get_estado(self):
        return self.estado

    def set_estado(self, estado):
        self.estado = estado


class Grupo:
    def __init__(self, presidente, sede):
        self.presidente = presidente
        self.sede = Pais(sede)

    def get_presidente(self):
        return self.presidente

    def set_presidente(self, presidente):
        self.presidente = presidente

    def get_sede(self):
        return self.sede

    def set_sede(self, sede):
        self.sede = sede

    def get_escolaridade_presidente_departamento(self):
        presidente = self.get_presidente()
        escolaridade = presidente.get_escolaridade()
        return escolaridade.get_escolariade()


class Empresa:
    def __init__(self, grupo, diretor):
        self.grupo = grupo
        self.diretor = diretor

    def get_grupo(self):
        return self.grupo

    def set_grupo(self, grupo):
        self.grupo = grupo

    def get_diretor(self):
        return self.diretor

    def set_diretor(self, diretor):
        self.diretor = diretor


class Filial:
    def __init__(self, empresa, cidade):
        self.empresa = empresa
        self.cidade = cidade

    def get_empresa(self):
        return self.empresa

    def set_empresa(self, empresa):
        self.empresa = empresa

    def get_cidade(self):
        return self.cidade

    def set_cidade(self, cidade):
        self.cidade = cidade

    def get_nome_diretor(self):
        empresa = self.get_empresa()
        diretor = empresa.get_diretor()
        return diretor.get_nome()


class Departamento:
    def __init__(self, empresa, chefia):
        self.empresa = empresa
        self.chefia = chefia

    def get_empresa(self):
        return self.empresa

    def set_empresa(self, empresa):
        self.empresa = empresa

    def get_chefia(self):
        return self.chefia

    def set_chefia(self, chefia):
        self.chefia = chefia

    def get_escolaridade_chefia(self):
        chefia = self.get_chefia()
        escolaridade = chefia.get_escolaridade()
        return escolaridade.get_escolariade()


class Funcionario:
    def __init__(self, nome, departamento, filial, escolaridade):
        self.nome = nome
        self.alocacao = departamento
        self.coordenacao = filial
        self.escolaridade = escolaridade

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_alocacao(self):
        return self.alocacao

    def set_alocacao(self, alocacao):
        self.alocacao = alocacao

    def get_coordenacao(self):
        return self.coordenacao

    def set_coordenacao(self, coordenacao):
        self.coordenacao = coordenacao

    def get_escolaridade(self):
        return self.escolaridade

    def set_escolaridade(self, escolaridade):
        self.escolaridade = escolaridade

    def get_pais_funcionario(self):
        departamento = self.get_alocacao()
        empresa = departamento.get_empresa()
        grupo = empresa.get_grupo()
        sede = grupo.get_sede()
        pais = sede.get_pais()
        return pais.get_pais()

    def get_estado_filial(self):
        filial = self.get_coordenacao()
        cidade = filial.get_cidade()
        estado = cidade.get_estado()
        return estado.get_estado()

class Escolaridade:
    def __init__(self, escolaridade):
        self.escolaridade = escolaridade

    def get_escolariade(self):
        return self.escolaridade

    def set_escolaridade(self, escolaridade):
        self.escolaridade = escolaridade


brasil = Pais("Brasil")
rio_de_janeiro = Estado("Rio de Janeiro", brasil)
vassouras = Cidade("Vassouras", rio_de_janeiro)
para = Estado("Pará", brasil)
belem = Cidade("Belém", para)

mestrado = Escolaridade("Mestrado")

fabrizzio = Funcionario("Fabrizzio", None, None, mestrado)
diego = Funcionario("Diego", None, None, mestrado)

gt_group = Grupo(fabrizzio, brasil)
node = Empresa(gt_group, diego)
dgtallab = Filial(node, belem)

presidencia = Departamento(node, fabrizzio)
direcao = Departamento(node, diego)

fabrizzio.set_alocacao(presidencia)
fabrizzio.set_coordenacao(dgtallab)
diego.set_alocacao(direcao)

print(f"Resposta 1: {gt_group.get_escolaridade_presidente_departamento()}")
print(f"Resposta 2: {diego.get_pais_funcionario()}")
print(f"Resposta 3: {fabrizzio.get_estado_filial()}")
print(f"Resposta 4: {direcao.get_escolaridade_chefia()}")
print(f"Resposta 5: {dgtallab.get_nome_diretor()}")
