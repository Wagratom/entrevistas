from ContaBancaria import ContaBancaria
from ExecOperationsConta import ExecOperationsConta

def handle_order_client(operation: ExecOperationsConta):
    while True:
        try:
            operation.show_options()
            operation.execute_order()
        except SystemExit:
            break
        except Exception as e:
            print(f"\033[91mErro: {e}\033[0m")


if __name__ == "__main__":
    op = ExecOperationsConta(None, None)
    conta1_saldo_inicial = op.get_input_value("Informe o saldo inicial da conta 1: R$")
    conta2_saldo_inicial = op.get_input_value("Informe o saldo inicial da conta 2: R$")
    conta1 = ContaBancaria(conta1_saldo_inicial)
    conta2 = ContaBancaria(conta2_saldo_inicial)

    handle_order_client(ExecOperationsConta(conta1, conta2))

