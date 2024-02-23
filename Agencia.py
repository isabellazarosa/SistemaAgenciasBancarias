class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print('Caixa abaixo do nível recomendado. Caixa Atual: {}'.format(self.caixa))
        else:
            print('O valor de Caixa está ok. Caixa Atual: {}'.format(self.caixa))

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print('Emprestimo não é possível. Dinheiro indisponível em caixa')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


class AgenciaVirtual(Agencia):  # Agencia virtual é subclasse de agencia
    def __init__(self, site, telefone, cnpj):
        self.site = site
        super().__init__(telefone, cnpj, 1000) # Roda o init da classe principal
        self.caixa = 1000000


class AgenciaComum(Agencia):
    pass


class AgenciaPremium(Agencia):
    pass


agencia1 = Agencia(33444555, 437463463468374, 4554)

agencia1.caixa = 1000000

agencia1.verificar_caixa()

agencia1.emprestar_dinheiro(1500, 827377389999, 0.03)

agencia1.adicionar_cliente('Isa', 11111111111, 10000)

print(agencia1.clientes)

agencia_virtual = AgenciaVirtual('ygygg', 222, 33333333333)

agencia_virtual.caixa = 15000
agencia_virtual.verificar_caixa()  # Herdou os métodos e atributos da superclasse

print(agencia_virtual.clientes)