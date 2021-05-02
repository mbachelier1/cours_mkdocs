def fibo_iteratif(n: int) -> int:
    a, b = 1, 1  # on initialise a = F0 et b = F1
    for _ in range(n - 1):
        a, b = b, a + b  # a devient b et b devient a + b
    return b
