from interfaces.ContaBancariaInterface import ContaBancariaInterface
from interfaces.CommandsInterface import CommandInterface

class DepositarItau(CommandInterface):
	def __init__(self, conta1: ContaBancariaInterface, valor: int):
		super().__init__(conta1, valor)
		self.taxa = 0.1

	def valid_number():
		
	def add_tax(self):
		self.valor = self.valor * (1 - self.taxa)

	def execute(self):
		try:
			self.add_tax()
			self.conta1.depositar(self.valor)
		except Exception as e:
			print(f"\033[91mErro: {e}\033[0m")

