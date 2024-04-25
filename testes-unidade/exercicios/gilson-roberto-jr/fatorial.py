def fatorial(n):
    if n < 0:
        raise ValueError("n cannot be a negative value.")

    return 1 if n == 0 else n * fatorial(n - 1)
