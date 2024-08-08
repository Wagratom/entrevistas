from interfaces.ContaBancariaInterface import ContaBancariaInterface
from interfaces.CommandsInterface import CommandInterface

class Sacar(CommandInterface):
	def __init__(self, conta1: ContaBancariaInterface, valor: int):
		super().__init__(conta1, valor)

	def execute(self):
		try:
			self.conta1.sacar(self.valor)
		except Exception as e:
			print(f"\033[91mErro: {e}\033[0m")
