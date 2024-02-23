from datetime import datetime
import pytz
from random import randint


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

    @staticmethod  # sinalizção para a pessoa ver que é estático
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')  # Método para formatar a tupla de data e hora recebida

    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome
        self.cpf = cpf
        self._saldo = 0  # underline diz que tem método para fazer todas as edições do objeto sem acessar ele direto
        self._limite = None  # Dois underline, torna inacessível fora da classe
        self.agencia = agencia
        self.num_conta = num_conta
        self._transacoes = []
        self.cartoes = []

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

    @staticmethod  # sinalizção para a pessoa ver que é estático
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR

    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000, 9999999999999999)  # Número aleatório que varia entre esses dois números
        self.titular = titular
        # Validade é data da criação mais 4 anos
        self.validade = '{}/{}'.format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year + 4)
        # Já que tem uns que começam com zero, então dá para usar esse truque
        self.cod_seguranca = '{}{}{}'.format(randint(0, 9), randint(0, 9), randint(0, 9))
        self.limite = 1000
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)  # Adiciona o cartão à lista de cartões da conta corrente
        # conta_corrente._cartoes.append(self) -- manda todas as informações do cartão para o objeto da conta corrente
        # conta_corrente._cartoes.append(self.numero) -- manda só o número do cartão para o objeto da conta corrente
        self._senha = 1234

    # Métodos com dois underlines só podem ser acessados a partir de outros métodos
    @property  # Para método getter
    def senha(self):
        return self._senha

    @senha.setter  # Para método setter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            print('Nova Senha Inválida')


