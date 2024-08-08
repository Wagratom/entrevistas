from interfaces.ContaBancariaInterface import ContaBancariaInterface
# resolvi aceitar o valor 0

class ContaBancaria(ContaBancariaInterface):
	def __init__(self, saldo_inicial=0):
		self.saldo = self.get_valid_number(saldo_inicial)
		if self.saldo < 0:
			raise Exception("Invalid initial balance. Account not created.")

	def get_valid_number(self, valor):
		try:
			return int(valor)
		except:
			raise Exception("Invalid value. Value must be an integer.")

	def depositar(self, valor):
		valor = self.get_valid_number(valor)
		if valor < 0:
			raise Exception("Invalid value for deposit. Deposit not performed.")

		self.saldo += valor
		print(f"Depósito de R${valor} realizado. Novo saldo: R${self.saldo}")

	def sacar(self, valor):
		valor = self.get_valid_number(valor)
		if valor < 0:
			raise Exception("Invalid value for withdrawal. Withdrawal not performed.")
		if self.saldo < valor:
			raise Exception("Insufficient balance. Operation not performed.")

		self.saldo -= valor
		print(f"Saque de R${valor} realizado. Novo saldo: R${self.saldo}")

	def transferir(self, destinatario, valor):
		valor = self.get_valid_number(valor)
		if valor < 0:
			raise Exception("Cannot transfer negative values!")
		if self.saldo < valor:
			raise Exception("Cannot transfer more than the balance!")

		self.saldo -= valor
		destinatario.depositar(valor)
		print(f"Transferencia de R$({valor}) realizada. Novo saldo: R${self.saldo}")
