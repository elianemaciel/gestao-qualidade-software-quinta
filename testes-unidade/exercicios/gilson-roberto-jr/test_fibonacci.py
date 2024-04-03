from fibonacci import fib


def test_fib_10():
    # Fibonacci sequence -> [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...]
    assert fib(10) == 55
