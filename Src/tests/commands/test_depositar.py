import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from commands.Depositar import Depositar
from ContaBancaria import ContaBancaria

class Randon():
	pass

class TesteDepositar(unittest.TestCase):
	########################
	# Valid deposit
	########################
	def test_depositar(self):
		conta = ContaBancaria()
		deposito = 500
		depositar = Depositar(conta, deposito)
		depositar.execute()
		self.assertEqual(conta.saldo,  (deposito * (1 - 0.1)))

	def test_depositar_2(self):
		conta = ContaBancaria()
		deposito = 1000
		depositar = Depositar(conta, deposito)
		depositar.execute()
		self.assertEqual(conta.saldo,  (deposito * (1 - 0.1)))


	########################
	# Invalid deposit
	########################
	def test_depositar_valor_invalido(self):
		conta = ContaBancaria()
		deposito = -500
		depositar = Depositar(conta, deposito)
		with self.assertRaises(Exception) as context:
			depositar.execute()
		self.assertEqual(str(context.exception), "Deposit value must be greater than 0")

	def test_depositar_valor_invalido_2(self):
		conta = ContaBancaria()
		deposito = 'a'
		depositar = Depositar(conta, deposito)
		with self.assertRaises(Exception) as context:
			depositar.execute()
		self.assertEqual(str(context.exception), "invalid literal for int() with base 10: 'a'")


	########################
	# Invalid account
	########################
	def test_depositar_conta_invalida(self):
		conta = Randon()
		deposito = 500
		depositar = Depositar(conta, deposito)
		with self.assertRaises(Exception) as context:
			depositar.execute()
		self.assertEqual(str(context.exception), "Invalid account")


if __name__ == '__main__':
	unittest.main()
