import pytest
from fatorial import fatorial


def test_n_equals_0():
    assert fatorial(0) == 1


def test_n_equals_1():
    assert fatorial(1) == 1


def test_n_positive():
    assert fatorial(5) == 120


def test_n_negative():
    with pytest.raises(ValueError):
        fatorial(-5)
