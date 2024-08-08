from ..ContaBancaria import ContaBancaria
import unittest


class TestOperations(unittest.TestCase):
	def test_depositar(self):
		conta1 = ContaBancaria(1000)
		conta1.depositar(500)
		self.assertEqual(conta1.saldo, 1500)

	def test_sacar(self):
		conta1 = ContaBancaria(1000)
		conta1.sacar(500)
		self.assertEqual(conta1.saldo, 500)

	def test_transferir(self):
		conta1 = ContaBancaria(1000)
		conta2 = ContaBancaria(1000)
		conta1.transferir(conta2, 500)
		self.assertEqual(conta1.saldo, 500)
		self.assertEqual(conta2.saldo, 1500)


	def test_depositar_valor_invalido(self):
		conta1 = ContaBancaria(1000)
		with self.assertRaises(Exception) as context:
			conta1.depositar(-500)
		self.assertEqual(str(context.exception), "Invalid value for deposit. Deposit not performed.")


	#########################
	# Invalid saques
	#########################
	def test_sacar_valor_invalido(self):
		conta1 = ContaBancaria(1000)
		with self.assertRaises(Exception) as context:
			conta1.sacar(-500)
		self.assertEqual(str(context.exception), "Invalid value for withdrawal. Withdrawal not performed.")

	def test_sacar_saldo_insuficiente(self):
		conta1 = ContaBancaria(1000)
		with self.assertRaises(Exception) as context:
			conta1.sacar(1500)
		self.assertEqual(str(context.exception), "Insufficient balance. Operation not performed.")


	#########################
	# Invalid transferencias
	#########################
	def test_transferir_valor_invalido(self):
		conta1 = ContaBancaria(1000)
		conta2 = ContaBancaria(1000)
		with self.assertRaises(Exception) as context:
			conta1.transferir(conta2, -500)
		self.assertEqual(str(context.exception), "Cannot transfer negative values!")

	def test_transferir_saldo_insuficiente(self):
		conta1 = ContaBancaria(1000)
		conta2 = ContaBancaria(1000)
		with self.assertRaises(Exception) as context:
			conta1.transferir(conta2, 1500)
		self.assertEqual(str(context.exception), "Cannot transfer more than the balance!")


	#########################
	# invalid initial balance
	#########################
	def test_saldo_inicial_invalido(self):
		with self.assertRaises(Exception) as context:
			ContaBancaria(-1000)
		self.assertEqual(str(context.exception), "Invalid initial balance. Account not created.")


	#########################
	# invalid integer
	#########################
	def test_invalid_integer(self):
		conta1 = ContaBancaria(1000)
		with self.assertRaises(Exception) as context:
			conta1.depositar("a")
		self.assertEqual(str(context.exception), "Invalid value. Value must be an integer.")

		with self.assertRaises(Exception) as context:
			conta1.sacar("b")
		self.assertEqual(str(context.exception), "Invalid value. Value must be an integer.")

		with self.assertRaises(Exception) as context:
			conta1.transferir(conta1, "c")
		self.assertEqual(str(context.exception), "Invalid value. Value must be an integer.")
if __name__ == "__main__":
	unittest.main()
