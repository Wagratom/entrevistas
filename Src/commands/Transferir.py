from interfaces.ContaBancariaInterface import ContaBancariaInterface
from interfaces.CommandsInterface import CommandInterface

class Transferir(CommandInterface):
	def __init__(self, conta1: ContaBancariaInterface, conta2: ContaBancariaInterface, valor: int):
		print('conta1', conta1)
		print('conta2', conta2)
		print('valor', valor)
		super().__init__(conta1, valor, conta2=conta2)

	def valid_number(self):
		int(self.valor)
		if self.valor < 0:
			raise ValueError("Transfer value must be greater than 0")

	def valid_account(self):
		if not self.conta1 or not self.conta2:
			raise ValueError("Account not found")
		if not isinstance(self.conta1, ContaBancariaInterface) or not isinstance(self.conta2, ContaBancariaInterface):
			raise ValueError("Invalid account")

	def valid_same_account(self):
		if self.conta1 == self.conta2:
			raise ValueError("Cannot transfer to the same account")

	def execute(self):
		self.valid_number()
		self.valid_account()
		self.valid_same_account()
		self.conta1.transferir(self.conta2, self.valor)
