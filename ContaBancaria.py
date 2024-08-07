# resolvi aceitar o valor 0
class ContaBancaria :
    def __init__(self, saldo_inicial=0):
        self.valid_integer(saldo_inicial)
        if saldo_inicial < 0:
            raise Exception("Invalid initial balance. Account not created.")
        self.saldo = saldo_inicial

    def valid_integer(self, valor):
        if (type(valor) != int):
            raise Exception("Invalid value. Value must be an integer.")

    def depositar(self, valor):
        self.valid_integer(valor)
        if valor < 0:
            raise Exception("Invalid value for deposit. Deposit not performed.")

        self.saldo += valor
        print(f"Depósito de R${valor} realizado. Novo saldo: R${self.saldo}")


    def sacar(self, valor):
        self.valid_integer(valor)
        if valor < 0:
            raise Exception("Invalid value for withdrawal. Withdrawal not performed.")
        if self.saldo < valor:
            raise Exception("Insufficient balance. Operation not performed.")

        self.saldo -= valor
        print(f"Saque de R${valor} realizado. Novo saldo: R${self.saldo}")

    def transferir(self, destinatario, valor):
        self.valid_integer(valor)
        if valor < 0:
            raise Exception("Cannot transfer negative values!")
        if self.saldo < valor:
            raise Exception("Cannot transfer more than the balance!")

        self.saldo -= valor
        destinatario.depositar(valor)
        print(f"Transferencia de R$({valor}) realizada. Novo saldo: R${self.saldo}")
