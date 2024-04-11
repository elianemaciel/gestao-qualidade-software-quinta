# Escreva testes para a função fatorial(n) para verificar se ela retorna o resultado correto para diferentes valores de n. Certifique-se de testar os seguintes casos:

#n igual a 0.
#n igual a 1.
#n igual a um número positivo maior que 1.
#n igual a um número negativo (nesse caso, a função deve lançar uma exceção). Use a biblioteca de testes padrão do Python, como unittest ou pytest, para escrever e executar os testes.
#Crie um PR com o código gerado (Nesse repositório) e peça a um colega para que faça a revisão.

import pytest

def fatorial(n):

    if n < 0:
        raise ValueError("O argumento deve ser um número inteiro não negativo.")
    if n == 0:
        return 1
    return n * fatorial(n - 1)

def test_fatorial_0():
    assert fatorial(0) == 1

def test_fatorial_1():
    assert fatorial(1) == 1

def test_fatorial_5():
    assert fatorial(5) == 120

def test_fatorial_negativo():
    with pytest.raises(ValueError):
        fatorial(-1)


