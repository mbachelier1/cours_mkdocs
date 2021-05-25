def aligne_naif(w1: str, w2: str) -> int:
    if not w1 or not w2:
        return len(w1) or len(w2)
    if w1[0] == w2[0]:
        return aligne_naif(w1[1:], w2[2:])
    else:
        return 1 + min(aligne_naif(w1, w2[1:]), aligne_naif(w1[1:], w2))


def aligne_dyn(w1: str, w2: str) -> int:
    if (w1, w2) in d:
        return d[w1, w2]
    elif not w1 or not w2:
        s = len(w1) or len(w2)
    elif w1[0] == w2[0]:
        s = aligne_dyn(w1[1:], w2[2:])
    else:
        s = 1 + min(aligne_dyn(w1, w2[1:]), aligne_dyn(w1[1:], w2))
    d[w1, w2] = s
    return s


def compte_tirets(w1, w2):
    resultat = 0
    for lettre in w1:
        if lettre == '-':
            resultat += 1
    for lettre in w2:
        if lettre == '-':
            resultat += 1
    return resultat


def aligne_str_naif(w1: str, w2: str):
    if not w1 or not w2:
        return len(w1) * '-', len(w2) * '-'
    if w1[0] == w2[0]:

        s1, s2 = aligne_str_naif(w1[1:], w2[1:])

        return w1[0] + s1, w2[0] + s2
    else:

        s1, s2 = aligne_str_naif(w1, w2[1:])
        s3, s4 = aligne_str_naif(w1[1:], w2)
        if compte_tirets(s1, s2) < compte_tirets(s3, s4):
            return '-' + s1, w2[0] + s2
        else:
            return w1[0] + s3, '-' + s4


def aligne_str_dyn(w1: str, w2: str):
    if (w1, w2) in d:
        return d[w1, w2]
    elif not w1 or not w2:
        s = len(w1) * '-', len(w2) * '-'
    elif w1[0] == w2[0]:
        s1, s2 = aligne_str_dyn(w1[1:], w2[1:])
        s = w1[0] + s1, w2[0] + s2
    else:
        s1, s2 = aligne_str_dyn(w1, w2[1:])
        s3, s4 = aligne_str_dyn(w1[1:], w2)
        if compte_tirets(s1, s2) < compte_tirets(s3, s4):
            s = '-' + s1, w2[0] + s2
        else:
            s = w1[0] + s3, '-' + s4
    d[w1, w2] = s
    return s


X = "INFORMATIQUE"
Y = "NUMERIQUE"
X = "TTCACCAGAAAAGAACACGGTAGTTACGAGTCCAATATTGTTAAACCG"
Y = "TTCACGAAAAAGTAACGGGCCGATCTCCAATAAGTGCGACCGAG"
d = dict()
print(aligne_dyn(X,Y))
d = dict()

assert(aligne_dyn("ATTGCAT","AGTCCAG")==6)

d = dict()
assert(aligne_dyn("GENOME","ENORME")==2)

d = dict()
assert(aligne_dyn("RESSORT","ESPRIT")==5)

"""
TTCACCAGAAAAGA--ACACGGTAGTTA-CGAG--TCCAATATT-GTTAA---ACC--G 
TTCA-C-GAAAA-AGTA-ACGG--G---CCGA-TCTCCAATA--AG-T--GCGACCGAG"""
