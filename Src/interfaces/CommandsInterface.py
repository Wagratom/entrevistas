from abc import ABC, abstractmethod
from .ContaBancariaInterface import ContaBancariaInterface

class CommandInterface(ABC):
    def __init__(self, conta1: ContaBancariaInterface, valor: int, conta2=None):
        self.conta1 = conta1
        self.conta2 = conta2
        self.valor = valor

    @abstractmethod
    def execute(self, valor):
        pass
