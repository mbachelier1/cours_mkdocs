def lev_naif(w1, w2):
    if not w1 or not w2:
        return len(w1) or len(w2)
    elif w1[-1] == w2[-1]:
        return lev_naif(w1[:-1], w2[:-1])
    else:
        return 1 + min(lev_naif(w1, w2[:-1]), lev_naif(w1[:-1], w2))


def leven(w1, w2):
    if (w1, w2) in d:
        return d[w1, w2]
    if not w1 or not w2:
        r = len(w1) or len(w2)
        d[w1, w2] = r
        return r
    elif w1[-1] == w2[-1]:
        r = leven(w1[:-1], w2[:-1])
        d[w1, w2] = r
        return r
    else:
        r = 1 + min(leven(w1, w2[:-1]), leven(w1[:-1], w2))
        d[w1, w2] = r
        return r


def lev_align(w1, w2):
    if (w1, w2) in d:
        return d[w1, w2]
    if not w1 or not w2:
        r = (len(w1 or w2), w1 or '-' * len(w1 or w2), w2 or '-' * len(w1 or w2))
        d[w1, w2] = r
        return r
    elif w1[-1] == w2[-1]:
        i = lev_align(w1[:-1], w2[:-1])
        r = (i[0], i[1] + w1[-1], i[2] + w2[-1])
        d[w1, w2] = r
        return r
    else:
        i, j = lev_align(w1, w2[:-1]), lev_align(w1[:-1], w2)
        if i[0] < j[0]:
            r = (1 + i[0], i[1] + '-', i[2] + w2[-1])
        else:
            r = (1 + j[0], j[1] + w1[-1], j[2] + '-')
        d[w1, w2] = r
        return r


d = dict()
X = "TTCACCAGAAAAGAACACGGTAGTTACGAGTCCAATATTGTTAAACCG"
Y = "TTCACGAAAAAGTAACGGGCCGATCTCCAATAAGTGCGACCGAG"

n,A,B = lev_align(X, Y)
C =[int(A[i]==B[i])*A[i] or ' ' for i in range(len(A))]
D = ''
for x in C :
    D += x
print(A)
print(D)
print(B)
"""
TTCACCAGAAAAGA--ACACGGTAGTTA-CGAG--TCCAATATT-GTTAA---ACC--G
TTCA-C-GAAAA-AGTA-ACGG--G---CCGA-TCTCCAATA--AG-T--GCGACCGAG
26
TTCAC-CAGAAAAG-AACACGGTAG-TTACGA--GTCCAAT-A-T--TGTTAAACC--G
TTCACG-A-AAAAGT-A-ACGG--GC---CGATC-TCCAATAAGTGC-G----ACCGAG
"""