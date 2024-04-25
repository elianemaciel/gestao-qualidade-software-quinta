def fib(n):
    seq = [0, 1]

    if n < 0:
        raise ValueError("n cannot be a negative value.")

    if n <= 1:
        return n

    for _ in range(2, n + 1):
        seq.append(seq[-2] + seq[-1])

    return seq[-1]
