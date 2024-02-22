from datetime import datetime
import pytz


class ContaCorrente():
    # Docstring -- ver no PEP 257 Docstring Conventions (colocar nos métodos também)
    # acessa usando help(ContaCorrente) no código, pode usar com qualquer biblioteca
    """
    Cria um objeto ContaCorrente para gerenciar as contas dos clientes.

    Atributos:
    nome (str): Nome do Cliente
    cpf (str): CPF do Cliente
    agencia (int): Agência responsável pela conta do Cliente
    num_conta (int): Número da conta do Cliente
    saldo: Saldo que há na conta do Cliente
    limite: Limite de Cheque especial do Cliente
    transacoes: Histórico de Transações do Cliente
    cartoes: Lista de Cartões do Cliente
    """

    @staticmethod  # sinalizção para a pessoa ver
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')  # Método para formatar a tupla de data e hora recebida

    def __init__(self, nome, cpf, agencia, num_conta):
        self._nome = nome  # underline diz que tem método para fazer todas as edições do objeto sem acessar ele direto
        self._cpf = cpf  # Dois underline, torna inacessível fora da classe
        self._saldo = 0
        self._limite = None
        self._agencia = agencia
        self._num_conta = num_conta
        self._transacoes = []
        self._cartoes = []

    def consultar_saldo(self):
        print('Seu saldo atual é de R${:,.2f}'.format(self._saldo))

    def depositar(self, valor):
        self._saldo += valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))

    def _limite_conta(self):
        # Por convesão métodos com underline são vistos como privados(se a pessoa tentar usar ele ela conseguirá)
        # Esse método não tem utilidade nenhuma para que usar a classe
        self._limite = -1000
        return self._limite

    def sacar(self, valor):
        if valor >= self._limite_conta():
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
            # Tive que passar como uma tupla no append, pois ele só aceita um argumento
        else:
            print('Você não tem saldo suficiente para sacar esse valor')
            self.consultar_saldo()

    def consultar_limite_cheque_especial(self):
        print('Seu limite de cheque especial é de R${:,.2f}'.format(self._limite_conta()))

    def consultar_historico_transacoes(self):
        print('Histórico de transações:')
        print('Valor, Saldo, Data e Hora')
        for transacao in self._transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):  # Não coloquei para verificar os limites
        self._saldo -= valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))
        conta_destino._saldo += valor
        conta_destino._transacoes.append((valor, conta_destino._saldo, ContaCorrente._data_hora()))


class CartaoCredito:

    def __init__(self, titular, conta_corrente):
        self.numero = 123  # None
        self.titular = titular
        self.validade = None
        self.cod_seguranca = None
        self.limite = None
        self.conta_corrente = conta_corrente
        conta_corrente._cartoes.append(self)  # Adiciona o cartão à lista de cartões da conta corrente
        # conta_corrente._cartoes.append(self) -- manda todas as informações do cartão para o objeto da conta corrente
        # conta_corrente._cartoes.append(self.numero) -- manda só o número do cartão para o objeto da conta corrente


# programa

conta_Isa = ContaCorrente("Isa", "999.999.999-99", 123, 11)

# # Depositando dinheiro na conta
# conta_Isa.depositar(10000)
#
# # Sacando dinheiro da conta
# # conta_Isa.sacar(10500)
#
# conta_Isa.consultar_saldo()
# conta_Isa.consultar_limite_cheque_especial()
# # print(conta_Isa.cpf)
#
# print('-' * 20)
#
# conta_Isa.consultar_historico_transacoes()
#
# print('-' * 20)
#
# conta_Adri = ContaCorrente('Adri', '111.111.111-11', 111, 22)
# conta_Isa.transferir(1000, conta_Adri)
#
# conta_Isa.consultar_saldo()
# conta_Adri.consultar_saldo()
#
# conta_Isa.consultar_historico_transacoes()
# conta_Adri.consultar_historico_transacoes()

cartao_Isa = CartaoCredito('Isa', conta_Isa)

print(cartao_Isa.conta_corrente._num_conta)

print(conta_Isa._cartoes[0].numero)
