from interfaces.ContaBancariaInterface import ContaBancariaInterface
from interfaces.CommandsInterface import CommandInterface

class Sacar(CommandInterface):
	def __init__(self, conta1: ContaBancariaInterface, valor: int):
		super().__init__(conta1, valor)

	def valid_number(self):
		int(self.valor)
		if self.valor < 0:
			raise ValueError("Withdraw value must be greater than 0")

	def valid_account(self):
		if not self.conta1:
			raise ValueError("Account not found")
		if not isinstance(self.conta1, ContaBancariaInterface):
			raise ValueError("Invalid account")

	def execute(self):
		self.valid_number()
		self.valid_account()
		self.conta1.sacar(self.valor)

