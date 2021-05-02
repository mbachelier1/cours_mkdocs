def levenshtein_naif(w1, w2):
    if not (w1 and w2):
        return max(len(w1), len(w2))
    elif w1[-1] == w2[-1]:
        return levenshtein_naif(w1[:-1], w2[:-1])
    else:
        return 1 + min(levenshtein_naif(w1[:-1], w2), levenshtein_naif(w1, w2[:-1]), levenshtein_naif(w1[:-1], w2[:-1]))


def levenshtein_dynamique_dict(w1, w2):
    if (w1, w2) in d:
        return d[w1, w2]
    if not (w1 and w2):
        r = max(len(w1), len(w2))

    elif w1[-1] == w2[-1]:
        r = levenshtein_dynamique_dict(w1[:-1], w2[:-1])

    else:
        r = 1 + min(levenshtein_dynamique_dict(w1[:-1], w2), levenshtein_dynamique_dict(w1, w2[:-1]),
                    levenshtein_dynamique_dict(w1[:-1], w2[:-1]))
    d[w1, w2] = r
    return r


def levenshtein_dynamique_matrice(w1, w2):
    n = len(w1)
    p = len(w2)
    matrice = [[0 for j in range(p + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        matrice[i][0] = i
    for j in range(p + 1):
        matrice[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, p + 1):
            if w1[i - 1] == w2[j - 1]:
                penalite = 0
            else:
                penalite = 1
            matrice[i][j] = min(matrice[i - 1][j] + 1, matrice[i][j - 1] + 1, matrice[i - 1][j - 1] + penalite)
    return matrice


def levenshtein_dynamique_chemin(matrice):
    chemin = []
    i = len(matrice) - 1
    j = len(matrice[0]) - 1
    while i > 0 or j > 0:
        print((i, j))
        chemin.append((i, j))
        valeurs_precedentes = []  # [matrice[i - 1][j], matrice[i][j - 1], matrice[i - 1, j - 1]]
        if i > 0:
            valeurs_precedentes.append(matrice[i - 1][j])
        if j > 0:
            valeurs_precedentes.append(matrice[i][j - 1])
        if i > 0 and j > 0:
            valeurs_precedentes.append(matrice[i - 1][j - 1])
        mini = min(valeurs_precedentes)
        indice = valeurs_precedentes.index(mini)
        if indice == 0:
            i -= 1
        elif indice == 1:
            j -= 1
        else:
            i -= 1
            j -= 1
    chemin.append((0, 0))
    chemin.reverse()
    return chemin


def levenshtein_dynamique_solution(w1, w2):
    matrice = levenshtein_dynamique_matrice(w1, w2)
    chemin = [(w1, w2)]
    i = len(matrice) - 1
    j = len(matrice[0]) - 1
    while i > 0 or j > 0:

        valeurs_precedentes = []  # [matrice[i - 1][j], matrice[i][j - 1], matrice[i - 1, j - 1]]
        if i > 0:
            valeurs_precedentes.append(matrice[i - 1][j])
        if j > 0:
            valeurs_precedentes.append(matrice[i][j - 1])
        if i > 0 and j > 0:
            valeurs_precedentes.append(matrice[i - 1][j - 1])
        mini = min(valeurs_precedentes)
        indice = valeurs_precedentes.index(mini)
        if indice == 0:
            i -= 1
            chemin.append()
        elif indice == 1:
            j -= 1
        else:
            i -= 1
            j -= 1

    chemin.reverse()
    return chemin


X = "NICHE"
Y = "CHIENS"

d = dict()
print(levenshtein_dynamique_dict(X, Y))
M = levenshtein_dynamique_matrice(X, Y)
print(M)
C = levenshtein_dynamique_chemin(M)
print(C)
print(levenshtein_dynamique_solution(X, Y, C))
# X = "TTCACCAGAAAAGAACACGGTAGTTACGAGTCCAATATTGTTAAACCG"
# Y = "TTCACGAAAAAGTAACGGGCCGATCTCCAATAAGTGCGACCGAG"
# print(levenshtein_naif(X, Y))
# d = dict()
# print(levenshtein_dynamique_dict(X, Y))
# print(levenshtein_dynamique_matrice(X, Y))
