from abc import ABC, abstractmethod

class ContaBancariaInterface(ABC):
    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def transferir(self, destinatario, valor):
        pass

    @abstractmethod
    def get_valid_number(self, valor):
        pass
