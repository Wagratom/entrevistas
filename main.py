from ContaBancaria import ContaBancaria

class Operations:

    def __init__(self, conta1: ContaBancaria, conta2: ContaBancaria):
        self.conta1 = conta1
        self.conta2 = conta2
        self.options = self.basic_options()
        self.operations = self.basic_operations()

    def basic_operations(self):
        return {
            "1": self.depositar,
            "2": self.sacar,
            "3": self.trasnferir
        }

    def basic_options(self):
        return  """
            Opções:
            1. Depositar
            2. Sacar
            3. Transferir
            4. Sair
        """

    def show_options(self):
        print(self.options)

    def add_option(self, option, function):
        self.operations[option] = function
        self.options += f"{option}. {function.__name__}\n"

    def get_option(self):
        return input('Escolha uma opção (1-4): ')

    def get_input_value(self, mensagem: str):
        while True:
            try:
                valor = float(input (mensagem))
                return valor
            except ValueError:
                 print(f"\033[91mPor favor, insira um valor numérico válido.\033[0m")

    def depositar(self):
        valor_deposito = self.get_input_value("Informe o valor a ser depositado na conta 1: R$")
        self.conta1.depositar(valor_deposito)

    def sacar(self):
        valor_saque = self.get_input_value("Informe o valor a ser sacado da conta 1: R$")
        self.conta1.sacar(valor_saque)

    def trasnferir(self):
        valor_transferencia = self.get_input_value("Informe o valor a ser transferido da conta 1 para a conta 2: R$")
        self.conta1.transferir(self.conta2, valor_transferencia)

    def exit(self):
        print("\nSaldos Finais:")
        print(f"Conta 1: R$ {self.conta1.saldo}")
        print(f"Conta 2: R$ {self.conta2.saldo}")
        print("\nObrigado por usar o sistema de contas bancárias!")
        raise SystemExit()

    def execute_order(self):
        order = self.get_option()

        if order in self.operations:
            self.operations[order]()
        elif order == "4":
            self.exit()
        else:
            print(f"\033[91mOpção inválida. Tente novamente.\033[0m")





def handle_order_client(operation: Operations):
    while True:
        try:
            operation.show_options()
            operation.execute_order()
        except SystemExit:
            break
        except Exception as e:
            print(f"\033[91mErro: {e}\033[0m")


if __name__ == "__main__":
    op = Operations(None, None)
    conta1_saldo_inicial = op.get_input_value("Informe o saldo inicial da conta 1: R$")
    conta2_saldo_inicial = op.get_input_value("Informe o saldo inicial da conta 2: R$")
    conta1 = ContaBancaria(conta1_saldo_inicial)
    conta2 = ContaBancaria(conta2_saldo_inicial)

    handle_order_client(Operations(conta1, conta2))

