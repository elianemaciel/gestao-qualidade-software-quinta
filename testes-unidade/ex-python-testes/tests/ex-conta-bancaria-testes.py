import unittest
from conta_bancaria import ContaBancaria

class TestContaBancaria(unittest.TestCase):
    def setUp(self):
        self.conta = ContaBancaria("Maria", 1000)

    def test_deposito(self):
        self.conta.depositar(500)
        self.assertEqual(self.conta.saldo, 1500)

    def test_saque_sucesso(self):
        self.conta.sacar(500)
        self.assertEqual(self.conta.saldo, 500)

    def test_saque_saldo_insuficiente(self):
        self.conta.sacar(1500)
        self.assertEqual(self.conta.saldo, 1000)  # O saldo deve permanecer inalterado

    def test_saque_valor_negativo(self):
        self.conta.sacar(-200)
        self.assertEqual(self.conta.saldo, 1000)  # O saldo deve permanecer inalterado

    def test_deposito_valor_negativo(self):
        self.conta.depositar(-200)
        self.assertEqual(self.conta.saldo, 1000)  # O saldo deve permanecer inalterado

    def test_consultar_saldo(self):
        saldo_atual = self.conta.saldo
        self.assertEqual(saldo_atual, self.conta.saldo)

if __name__ == '__main__':
    unittest.main()
