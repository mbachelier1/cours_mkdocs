import sys
import matplotlib.pyplot as plt

s = {1: 1, 2: 2}


def Q(n: int) -> int:
    if n in s:
        return s[n]
    else:
        c = Q(n - 1)
        d = Q(n - 2)
        r = Q(n - c) + Q(n - d)
        s[n] = r
        return r


t = [None] * 10000
t[1] = 1
t[2] = 1


def Q2(n: int) -> int:
    if t[n]:
        return t[n]
    else:
        c = Q(n - 1)
        d = Q(n - 2)
        r = Q(n - c) + Q(n - d)
        t[n] = r
        return r


sys.setrecursionlimit(10_000)
print(Q2(3000))
"""
a = .5
X = list(range(1, 2000))
Y = [s[i] for i in X]
Z = [a * i for i in X]
plt.plot(X, Y)
plt.plot(X, Z)
plt.show()
"""