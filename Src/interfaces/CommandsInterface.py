from abc import ABC, abstractmethod
from .ContaBancariaInterface import ContaBancariaInterface

class DepositarInterface(ABC):
	def __init__(self, conta: ContaBancariaInterface, valor: int):
		self.conta = conta
		self.valor = valor

	@abstractmethod
	def execute(self):
		pass


class SacarInterface(ABC):
	def __init__(self, conta: ContaBancariaInterface, valor: int):
		self.conta = conta
		self.valor = valor

	@abstractmethod
	def execute(self):
		pass


class TransferirInterface(ABC):
	def __init__(self, conta1: ContaBancariaInterface, conta2: ContaBancariaInterface, valor: int):
		self.conta1 = conta1
		self.conta2 = conta2
		self.valor = valor

	@abstractmethod
	def execute(self):
		pass
