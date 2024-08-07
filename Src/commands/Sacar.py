from ..interfaces.CommandsInterface import CommandsInterface
from ..interfaces.ContaBancariaInterface import ContaBancariaInterface

class Sacar(CommandsInterface):
	def __init__(self, conta1: ContaBancariaInterface, valor: int):
		super().__init__(conta1, valor)

	def validate_value(self):
		value = int(self.valor)
		if value < 0:
			raise ValueError("O valor do saque deve ser maior que zero.")
		return value

	def execute(self):
		try:
			self.validate_value()
			self.conta1.sacar(self.valor)
			return True
		except ValueError as e:
			print(f"\033[91mErro: {e}\033[0m")
			return False
