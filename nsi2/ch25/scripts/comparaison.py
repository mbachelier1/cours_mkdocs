import matplotlib.pyplot as plt

def fibo_dynamique(n):
    global nb_opel
    if n in d:
        return d[n]
    elif n < 2:
        d[n] = 1
        return 1
    else:

        d[n] = fibo_dynamique(n - 1) + fibo_dynamique(n - 2)
        return d[n]


def fibo_naif(n):
    global nb_opel
    if n < 2:
        return 1
    else:
        nb_opel += 1
        return fibo_naif(n - 1) + fibo_naif(n - 2)


d = dict()
nb_opel = 0
X, Y, Z = [], [], []
for i in range(1, 25):
    X.append(i)
    nb_opel = 0
    fibo_naif(i)
    Y.append(nb_opel)
    nb_opel = 0
    fibo_dynamique(i)
    Z.append(nb_opel)

plt.plot(X,Y)
plt.plot(X,Z)
plt.show()