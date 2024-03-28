import pytest
import ContaBancaria


@pytest.fixture
def conta_bancaria():
    return ContaBancaria.ContaBancaria("Maria", 1000)


def test_deposito(conta_bancaria):
    conta_bancaria.depositar(500)
    assert conta_bancaria.saldo == 1500


def test_saque_sucesso(conta_bancaria):
    conta_bancaria.sacar(500)
    assert conta_bancaria.saldo == 500


def test_saque_saldo_insuficiente(conta_bancaria):
    pass


def test_saque_valor_negativo(conta_bancaria):
    pass


def test_deposito_valor_negativo(conta_bancaria):
    pass


def test_consultar_saldo(conta_bancaria):
    pass
