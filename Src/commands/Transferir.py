from interfaces.ContaBancariaInterface import ContaBancariaInterface
from interfaces.CommandsInterface import CommandInterface

class Transferir(CommandInterface):
	def __init__(self, conta1: ContaBancariaInterface, conta2: ContaBancariaInterface, valor: int):
		super().__init__(conta1, conta2, valor)

	def execute(self):
		try:
			self.conta1.transferir(self.conta2, self.valor)
		except Exception as e:
			print(f"\033[91mErro: {e}\033[0m")
