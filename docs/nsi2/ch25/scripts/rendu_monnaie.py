def rendu(somme):
    if somme in liste_pieces:
        return 1
    else:
        return 1 + min(rendu(somme - piece) for piece in liste_pieces if piece <= somme)


def rendu_dyn(somme):
    if somme in solutions:
        return solutions[somme]
    if somme in liste_pieces:
        solutions[somme] = 1
    else:
        solutions[somme] = 1 + min(rendu_dyn(somme - piece) for piece in liste_pieces if piece <= somme)
    return solutions[somme]

def rendu_dyn(somme,liste = None):
    if somme in solutions:
        return solutions[somme]
    if somme in liste_pieces:
        solutions[somme] = 1
    else:
        solutions[somme] = 1 + min(rendu_dyn(somme - piece) for piece in liste_pieces if piece <= somme)
    return solutions[somme]


liste_pieces = [1, 2, 5, 10]
solutions = dict()
print(rendu_dyn(30))