def size(n: int) -> int:
    s = 0
    while n:
        s += 1
        n //= 2
    return s


def karatsuba(x, y, n=None):
    if n is None:
        n = max(size(x), size(y))
    if n <= 1:
        return x * y
    else:
        n //= 2
        m = 1 << n
        a, b = x >> n, x % m
        c, d = y >> n, y % m
        ac = karatsuba(a, c, n)
        bd = karatsuba(b, d, n)
        p = karatsuba(a - b, c - d, n)
        return (ac << (2 * n)) + ((ac + bd - p) << n) + bd
