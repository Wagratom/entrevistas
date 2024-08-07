from ..interfaces.ContaBancariaInterface import ContaBancariaInterface
from ..interfaces.CommandsInterface import DepositarInterface

class DepositarNubank(DepositarInterface):
	def __init__(self, conta1, valor):
		super().__init__(conta1, valor)

	def validate_value(self):
		value = int(self.valor)
		if value < 0:
			raise ValueError("O valor do depósito deve ser maior que zero.")
		return value

	def add_tax(self):
		self.valor = self.valor * (1 - self.taxa)

	def execute(self):
		try:
			self.validate_value()
			self.add_tax()
			self.conta1.depositar(self.valor)
			return True
		except ValueError as e:
			print(f"\033[91mErro: {e}\033[0m")
			return False


# class DepositarItau(CommandsInterface):
# 	def __init__(self, conta2):
# 		self.conta2 = conta2

# 	def value_deposit(self):
# 		valor_deposito = self.get_input_value("Informe o valor a ser depositado na conta 2: R$")
# 		if valor_deposito < 0:
# 			raise ValueError("O valor do depósito deve ser maior que zero.")
# 		return valor_deposito

# 	def execute(self):
# 		try:
# 			valor_deposito = self.value_deposit()
# 			self.conta2.depositar(valor_deposito)
# 			return True
# 		except ValueError as e:
# 			print(f"\033[91mErro: {e}\033[0m")
# 			return False
