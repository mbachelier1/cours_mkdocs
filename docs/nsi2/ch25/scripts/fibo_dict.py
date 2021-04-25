def fibo_dyn2(n):
    if n in d:
        return d[n]
    elif n < 2:
        d[n] = 1
        return 1
    else:
        d[n] = fibo_dyn2(n - 1) + fibo_dyn2(n - 2)
        return d[n]


d = dict()
print(fibo_dyn2(10))

