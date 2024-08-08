import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from commands.Transferir import Transferir
from ContaBancaria import ContaBancaria

class Randon():
	pass

class TesteTransferir(unittest.TestCase):

	########################
	# Valid transfer
	########################
	def test_valid_transfer(self):
		conta_origem = ContaBancaria(1000)
		conta_destino = ContaBancaria(0)
		valor_transferencia = 500
		Transferir(conta_origem, conta_destino, valor_transferencia).execute()

		self.assertEqual(conta_origem.saldo, 500)
		self.assertEqual(conta_destino.saldo, 500)

	def test_valid_transfer_2(self):
		conta_origem = ContaBancaria(1000)
		conta_destino = ContaBancaria(0)
		valor_transferencia = 1000
		Transferir(conta_origem, conta_destino, valor_transferencia).execute()

		self.assertEqual(conta_origem.saldo, 0)
		self.assertEqual(conta_destino.saldo, 1000)

	def test_valid_transfer_3(self):
		conta_origem = ContaBancaria(1000)
		conta_destino = ContaBancaria(0)
		valor_transferencia = 0
		Transferir(conta_origem, conta_destino, valor_transferencia).execute()


		self.assertEqual(conta_origem.saldo, 1000)
		self.assertEqual(conta_destino.saldo, 0)

	########################
	# Invalid transfer
	########################
	def test_invalid_transfer_insufficient_funds(self):
		conta_origem = ContaBancaria(100)
		conta_destino = ContaBancaria(0)
		valor_transferencia = 200

		with self.assertRaises(Exception) as context:
			Transferir(conta_origem, conta_destino, valor_transferencia).execute()
		self.assertEqual(str(context.exception), "Cannot transfer more than the balance!")

	def test_invalid_transfer_negative_amount(self):
		conta_origem = ContaBancaria(1000)
		conta_destino = ContaBancaria(0)
		valor_transferencia = -200

		with self.assertRaises(ValueError) as context:
			Transferir(conta_origem, conta_destino, valor_transferencia).execute()
		self.assertEqual(str(context.exception), "Transfer value must be greater than 0")

	def test_invalid_transfer_same_account(self):
		conta_origem = ContaBancaria(1000)
		conta_destino = conta_origem
		valor_transferencia = 500

		with self.assertRaises(ValueError) as context:
			Transferir(conta_origem, conta_destino, valor_transferencia).execute()
		self.assertEqual(str(context.exception), "Cannot transfer to the same account")

	def test_invalid_firt_account(self):
		conta_origem = Randon()
		conta_destino = ContaBancaria(0)
		valor_transferencia = 500

		with self.assertRaises(ValueError) as context:
			Transferir(conta_origem, conta_destino, valor_transferencia).execute()
		self.assertEqual(str(context.exception), "Invalid account")

	def test_invalid_second_account(self):
		conta_origem = ContaBancaria(1000)
		conta_destino = Randon()
		valor_transferencia = 500

		with self.assertRaises(ValueError) as context:
			Transferir(conta_origem, conta_destino, valor_transferencia).execute()
		self.assertEqual(str(context.exception), "Invalid account")
if __name__ == '__main__':
	unittest.main()
