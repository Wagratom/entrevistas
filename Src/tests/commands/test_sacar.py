import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from commands.Sacar import Sacar
from ContaBancaria import ContaBancaria

class Randon():
	pass

class TesteSacar(unittest.TestCase):
	########################
	# Valid withdraw
	########################
	def test_sacar(self):
		conta = ContaBancaria(1000)
		saque = 500
		sacar = Sacar(conta, saque)
		sacar.execute()
		self.assertEqual(conta.saldo,  500)

	def test_sacar_2(self):
		conta = ContaBancaria(1000)
		saque = 1000
		sacar = Sacar(conta, saque)
		sacar.execute()
		self.assertEqual(conta.saldo,  0)

	def teste_sacar_3(self):
		conta = ContaBancaria(1000)
		saque = 0
		sacar = Sacar(conta, saque)
		sacar.execute()
		self.assertEqual(conta.saldo,  1000)

	########################
	# Invalid withdraw
	########################

	def test_sacar_valor_negativo(self):
		conta = ContaBancaria(1000)
		saque = -500
		sacar = Sacar(conta, saque)
		with self.assertRaises(Exception) as context:
			sacar.execute()
		self.assertEqual(str(context.exception), "Withdraw value must be greater than 0")

	def test_sacar_valor_letra(self):
		conta = ContaBancaria(1000)
		saque = 'a'
		sacar = Sacar(conta, saque)
		with self.assertRaises(Exception) as context:
			sacar.execute()
		self.assertEqual(str(context.exception), "invalid literal for int() with base 10: 'a'")

	def teste_sacar_valor_saldo_insuficiente(self):
		conta = ContaBancaria(1000)
		saque = 1500
		sacar = Sacar(conta, saque)
		with self.assertRaises(Exception) as context:
			sacar.execute()
		self.assertEqual(str(context.exception), "Insufficient balance. Operation not performed.")

	########################
	# Invalid account
	########################
	def test_sacar_conta_invalida(self):
		conta = Randon()
		saque = 500
		sacar = Sacar(conta, saque)
		with self.assertRaises(Exception) as context:
			sacar.execute()
		self.assertEqual(str(context.exception), "Invalid account")
if __name__ == '__main__':
	unittest.main()
