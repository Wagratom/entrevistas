from ..interfaces.CommandsInterface import CommandsInterface
from ..interfaces.ContaBancariaInterface import ContaBancariaInterface

class Transferir(CommandsInterface):
	def __init__(self, conta1: ContaBancariaInterface, conta2: ContaBancariaInterface, valor: int):
		super().__init__(conta1, conta2, valor)

	def validate_value(self):
		value = int(self.valor)
		if value < 0:
			raise ValueError("O valor do saque deve ser maior que zero.")
		return value

	def execute(self):
		try:
			self.validate_value()
			self.conta1.transferir(self.conta2, self.valor)
			return True
		except ValueError as e:
			print(f"\033[91mErro: {e}\033[0m")
			return False
		except Exception as e:
			print(f"\033[91mErro: {e}\033[0m")
			return False
