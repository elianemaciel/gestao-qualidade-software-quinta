class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R${valor:.2f} realizado com sucesso.')
        else:
            print('O valor do depósito deve ser maior que zero.')

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R${valor:.2f} realizado com sucesso.')
        elif valor <= 0:
            print('O valor do saque deve ser maior que zero.')
        else:
            print('Saldo insuficiente.')

    def consultar_saldo(self):
        print(f'Saldo disponível: R${self.saldo:.2f}')


# Exemplo de uso da classe
if __name__ == "__main__":
    # Criando uma conta bancária
    minha_conta = ContaBancaria("João")

    # Fazendo operações na conta
    minha_conta.consultar_saldo()
    minha_conta.depositar(1000)
    minha_conta.consultar_saldo()
    minha_conta.sacar(500)
    minha_conta.consultar_saldo()
    minha_conta.sacar(700)
    minha_conta.depositar(-100)  # Tentativa de depósito inválida
