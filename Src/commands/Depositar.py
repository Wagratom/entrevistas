from interfaces.ContaBancariaInterface import ContaBancariaInterface
from interfaces.CommandsInterface import CommandInterface

class DepositarItau(CommandInterface):
	def __init__(self, conta1: ContaBancariaInterface, valor: int):
		super().__init__(conta1, valor)
		self.taxa = 0.1

	def valid_number(self):
		int(self.valor)
		if self.valor < 0:
			raise ValueError("Deposit value must be greater than 0")

	def valid_account(self):
		if not self.conta1:
			raise ValueError("Account not found")
		if not isinstance(self.conta1, CommandInterface):
			raise ValueError("Invalid account")

	def add_tax(self):
		self.valor = self.valor * (1 - self.taxa)

	def execute(self):
		try:
			self.add_tax()
			self.valid_number()
			self.conta1.depositar(self.valor)
		except ValueError as e:
			print(f"\033[91mErro: {e}\033[0m")
		except Exception as e:
			print(f"\033[91mErro: {e}\033[0m")
