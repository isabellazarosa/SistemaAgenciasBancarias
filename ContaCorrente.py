class ContaCorrente():

    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta

    def consultar_saldo(self):
        print('Seu saldo atual é de R${:,.2f}'.format(self.saldo))

    def depositar(self,valor):
        self.saldo += valor

    def _limite_conta(self):
    # Por convesão métodos com underline no ínicio são vistos como privados(se a pessoa tentar usar ele ela conseguirá)
    # Esse método não tem utilidade nenhuma para que usar a classe
        self.limite = -1000
        return self.limite

    def sacar(self, valor):
        if self.saldo - valor < self._limite_conta():
            print('Você não tem saldo suficiente para sacar esse valor')
            self.consultar_saldo()
        else:
            self.saldo -= valor

    def consultar_limite_cheque_especial(self):
        print('Seu limite de cheque especial é de R${:,.2f}'.format(self._limite_conta()))


#programa

conta_Isa = ContaCorrente("Isa", "999.999.999-99", 123, 11)


#print(conta_Isa.consultar_saldo)
conta_Isa.depositar(10000)
conta_Isa.sacar(10500)
conta_Isa.consultar_saldo()
conta_Isa.consultar_limite_cheque_especial()
#print(conta_Isa.cpf)
