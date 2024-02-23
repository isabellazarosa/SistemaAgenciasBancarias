from ContaCorrente import ContaCorrente, CartaoCredito
from Agencia import AgenciaPremium, AgenciaComum, AgenciaVirtual

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

# print(cartao_Isa.conta_corrente._num_conta)

# print(conta_Isa._cartoes[0].numero)

print(cartao_Isa.validade)
print(cartao_Isa.numero)
print(cartao_Isa.cod_seguranca)

cartao_Isa.senha = '1245'
print(cartao_Isa.senha)

print(conta_Isa.__dict__)  # Esse método lista todos atributos e valores das estâncias que a classe tem
print(cartao_Isa.__dict__)

agencia_premium_especial = AgenciaPremium(7777777, 888888)
print(agencia_premium_especial.caixa)
