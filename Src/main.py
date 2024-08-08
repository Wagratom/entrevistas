from ContaBancaria import ContaBancaria
from interfaces.ContaBancariaInterface import ContaBancariaInterface
from commands.Depositar import DepositarItau as depositar
from commands.Sacar import Sacar as sacar
from commands.Transferir import Transferir as transferir
import sys

class HandleOperations:
	def __init__(self, conta1: ContaBancariaInterface, conta2: ContaBancariaInterface):
		self.conta1 = conta1
		self.conta2 = conta2
		self.operations = {
			"1": self.depositar,
			"2": self.sacar,
			"3": self.transferir,
			"4": self.exit
		}

	def show_options(self):
		options = (
			"Opções:\n"
			"\n"
			"1. Depositar\n"
			"2. Sacar\n"
			"3. Transferir\n"
			"4. Sair\n"
		)
		print(options)

	def get_option(self):
		return input('Escolha uma opção (1-4): ')

	def show_data(self):
		print(f"Saldo da conta 1: R$ {self.conta1.saldo}")
		print(f"Saldo da conta 2: R$ {self.conta2.saldo}\n")

	@staticmethod
	def get_input_value(mensagem: str):
		while True:
			try:
				valor = float(input(mensagem))
				return valor
			except ValueError:
				print(f"\033[91mPor favor, insira um valor numérico válido.\033[0m")

	def execute(self, command):
		if command in self.operations:
			self.operations[command]()
		else:
			print(f"\033[91mOpção inválida. Tente novamente.\033[0m")

	def depositar(self):
		value = self.get_input_value("Informe o valor a ser depositado: R$")
		command = depositar(self.conta1, value)
		command.execute()

	def sacar(self):
		value = self.get_input_value("Informe o valor a ser sacado: R$")
		command = sacar(self.conta1, value)
		command.execute()

	def transferir(self):
		value = self.get_input_value("Informe o valor a ser transferido: R$")
		command = transferir(self.conta1, value, self.conta2)
		command.execute()

	def exit(self):
		print("\nSaldos Finais:")
		self.show_data()
		print("\nObrigado por usar o sistema de contas bancárias!")
		sys.exit(0)

	def execute_routine(self):
		while True:
			try:
				self.show_options()
				order = self.get_option()
				self.execute(order)
			except Exception as e:
				print(f"\033[91mErro: {e}\033[0m")


if __name__ == "__main__":
	conta1_saldo_inicial = HandleOperations.get_input_value("Informe o saldo inicial da conta 1: R$")
	conta2_saldo_inicial = HandleOperations.get_input_value("Informe o saldo inicial da conta 2: R$")
	conta1 = ContaBancaria(conta1_saldo_inicial)
	conta2 = ContaBancaria(conta2_saldo_inicial)
	HandleOperations(conta1, conta2).execute_routine()

