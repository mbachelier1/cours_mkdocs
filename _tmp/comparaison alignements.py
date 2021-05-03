def aligne_naif(w1: str, w2: str) -> int:
    # par la fin
    if not w1 or not w2:
        return len(w1) or len(w2)
    if w1[-1] == w2[-1]:
        return aligne_naif(w1[:-1], w2[:-1])
    else:
        return 1 + min(aligne_naif(w1, w2[:-1]), aligne_naif(w1[:-1], w2))


# PAR LE DEBUT

def aligne_naif2(w1: str, w2: str) -> int:
    # par le début
    if not w1 or not w2:
        return len(w1) or len(w2)
    if w1[0] == w2[0]:
        return aligne_naif(w1[1:], w2[1:])
    else:
        return 1 + min(aligne_naif2(w1, w2[1:]), aligne_naif2(w1[1:], w2))


d = dict()
def aligne_rec_dyn(w1: str, w2: str) -> int:
    # par le début
    if (w1, w2) in d:
        return d[w1, w2]
    elif not w1 or not w2:
        s = len(w1) or len(w2)
    elif w1[0] == w2[0]:
        s = aligne_rec_dyn(w1[1:], w2[1:])
    else:
        s = 1 + min(aligne_rec_dyn(w1, w2[1:]), aligne_rec_dyn(w1[1:], w2))
    d[w1, w2] = s
    return s


def aligne_rec_dyn_liste(w1: str, w2: str) -> tuple:
    # par le début
    if (w1, w2) in d:
        return d[w1, w2]
    elif not w1 or not w2:
        s = (len(w1) or len(w2), len(w1) * '-', len(w2) * '-')
    elif w1[0] == w2[0]:
        s0, s1, s2 = aligne_rec_dyn_liste(w1[1:], w2[1:])
        s = (s0, w1[0] + s1, w2[0] + s2)
    else:
        s0, s1, s2, = aligne_rec_dyn_liste(w1, w2[1:])
        s3, s4, s5 = aligne_rec_dyn_liste(w1[1:], w2)
        if s0 <= s3:
            s = (1 + s0, '-' + s1, w2[0] + s2)
        else:
            s = (1 + s3, w1[0] + s4, '-' + s5)
    d[w1, w2] = s
    return s


# ---------------------

def aligner_rec(x, y, i, j):
    '''renvoie le score(nbre de trous minimal)
    de x et y'''
    if i == 0:  # si la chaine x est vide
        return j
    elif j == 0:
        return i
    else:
        # on s'intéresse au dernier caractère
        if x[i - 1] == y[j - 1]:
            return aligner_rec(x, y, i - 1, j - 1)
        else:
            return 1 + min(aligner_rec(x, y, i, j - 1), aligner_rec(x, y, i - 1, j))


def aligner_dyn(x, y):
    n = len(x) + 1
    m = len(y) + 1
    score = [[0 for _ in range(m)] for _ in range(n)]  # tableau des scores

    # score lorsque j=0
    for i in range(n):
        score[i][0] = i

    # score lorsque i=0
    for j in range(m):
        score[0][j] = j

    # score[i][j] sinon
    for i in range(1, n):
        for j in range(1, m):
            score[i][j] = 1 + min(score[i][j - 1], score[i - 1][j]) if x[i - 1] != y[j - 1] else score[i - 1][j - 1]
    return score[n - 1][m - 1]


def aligner_dyn_affiche(x, y):
    n = len(x) + 1
    m = len(y) + 1
    score = [[(0, '', '') for _ in range(m)] for _ in range(n)]  # tableau des scores et des motifs obtenus

    for i in range(n):
        score[i][0] = (i, x[:i], '-' * i)

    for j in range(m):
        score[0][j] = (j, '-' * j, y[:j])

    for i in range(1, n):
        for j in range(1, m):
            if x[i - 1] == y[j - 1]:
                total, xmotif, ymotif = score[i - 1][j - 1]
                score[i][j] = (total, xmotif + x[i - 1], ymotif + y[j - 1])
            else:
                total1, xmotif1, ymotif1 = score[i][j - 1]
                total2, xmotif2, ymotif2 = score[i - 1][j]

                if total1 <= total2:
                    total = 1 + total1
                    xmotif = xmotif1 + '-'
                    ymotif = ymotif1 + y[j - 1]
                else:
                    total = 1 + total2
                    xmotif = xmotif2 + x[i - 1]
                    ymotif = ymotif2 + '-'

                score[i][j] = (total, xmotif, ymotif)

    return score[n - 1][m - 1]


X = "TTCACCAGAAAAGAACACGGTAGTTACGAGTCCAATATTGTTAAACCG"
Y = "TTCACGAAAAAGTAACGGGCCGATCTCCAATAAGTGCGACCGAG"

X = "AADBBDCDBACDCCDBACDBCABCDABCDABCDABCD"
Y = "ACBDACBDACCDCDBABABDCABCBCDBDBDCABDCBDACBD"
s,x,y = aligne_rec_dyn_liste(X, Y)
print(s)
print(x)
print(y)

s,x,y = aligner_dyn_affiche(X, Y)
print(s)
print(x)
print(y)
