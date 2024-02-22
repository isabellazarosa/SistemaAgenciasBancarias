from datetime import datetime
import pytz


class ContaCorrente():

    @staticmethod  # sinalizção para a pessoa ver
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')  # Método para formatar a tupla de data e hora recebida

    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes = []

    def consultar_saldo(self):
        print('Seu saldo atual é de R${:,.2f}'.format(self.saldo))

    def depositar(self, valor):
        self.saldo += valor
        self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))

    def _limite_conta(self):
        # Por convesão métodos com underline são vistos como privados(se a pessoa tentar usar ele ela conseguirá)
        # Esse método não tem utilidade nenhuma para que usar a classe
        self.limite = -1000
        return self.limite

    def sacar(self, valor):
        if self.saldo - valor < self._limite_conta():
            print('Você não tem saldo suficiente para sacar esse valor')
            self.consultar_saldo()
        else:
            self.saldo -= valor
            self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))
            # Tive que passar como uma tupla no append, pois ele só aceita um argumento

    def consultar_limite_cheque_especial(self):
        print('Seu limite de cheque especial é de R${:,.2f}'.format(self._limite_conta()))

    def consultar_historico_transacoes(self):
        print('Histórico de transações:')
        print('Valor, Saldo, Data e Hora')
        for transacao in self.transacoes:
            print(transacao)


# programa

conta_Isa = ContaCorrente("Isa", "999.999.999-99", 123, 11)

# Depositando dinheiro na conta
conta_Isa.depositar(10000)

# Sacando dinheiro da conta
conta_Isa.sacar(10500)

conta_Isa.consultar_saldo()
conta_Isa.consultar_limite_cheque_especial()
# print(conta_Isa.cpf)

print('-' * 20)

conta_Isa.consultar_historico_transacoes()
