import os
from time import sleep

BLACK_FG = '[30m'
RED_FG = '[31m'
GREEN_FG = '[32m'
YELLOW_FG = '[33m'
BLUE_FG = '[34m'
MAGENTA_FG = '[35m'
CYAN_FG = '[36m'
WHITE_FG = '[37m'
BLACK_BG = '[40m'
RED_BG = '[41m'
GREEN_BG = '[42m'
YELLOW_BG = '[43m'
BLUE_BG = '[44m'
MAGENTA_BG = '[45m'
CYAN_BG = '[46m'
WHITE_BG = '[47m'
RST = '[0m'


def clear() -> None:
    """
    Clears console
    """
    os.system('cls')


def echo(string) -> None:
    """
    Displays a message in the console
    :param string: str
    """
    os.system('echo ' + str(string) + RST)


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


def creer_solution(mot1, mot2):
    r, s1, s2 = aligner_dyn_affiche(mot1, mot2)
    echo(' ')
    echo(' ')

    echo('  ' + s1)
    echo('  ' + s2)
    echo(' ')
    echo(' ')
    input()
    sleep(1)
    echo('x')
    sleep(1)
    echo('x')
    sleep(1)
    clear()
    sleep(1)
    i = 0
    j = 0
    debut1 = BLUE_FG
    debut2 = BLUE_FG
    clear()
    echo(' ')
    echo(' ')

    echo('  ' + BLUE_FG + mot1)
    echo('  ' + BLUE_FG + mot2)
    echo(' ')
    echo(' ')
    sleep(1)

    for k in range(len(s1)):
        lettre1 = s1[k]
        lettre2 = s2[k]
        if lettre1 != '-':
            i += 1
        if lettre2 != '-':
            j += 1
        if lettre1 == lettre2:
            debut1 += RED_FG + lettre1 + BLUE_FG
            debut2 += RED_FG + lettre1 + BLUE_FG
        else:
            debut1 += lettre1
            debut2 += lettre2
        clear()
        echo(' ')
        echo(' ')

        echo('  ' + debut1 + BLUE_FG + mot1[i:] + RST)
        echo('  ' + debut2 + BLUE_FG + mot2[j:] + RST)
        echo('  ' + ' ' * k + '^^')
        echo(' ')
        echo(' ')

        sleep(0.5)


X = "TTCACCAGAAAAGAACACGGTAGTTACGAGTCCAATATTGTTAAACCG"
Y = "TTCACGAAAAAGTAACGGGCCGATCTCCAATAAGTGCGACCGAG"


creer_solution(X, Y)

input()
