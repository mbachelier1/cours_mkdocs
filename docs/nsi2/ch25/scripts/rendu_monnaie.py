def rendu(somme):
    if somme in liste_valeurs:
        return 1
    else:
        return 1 + min(rendu(somme - piece) for piece in liste_valeurs if piece <= somme)


def rendu_rec_dyn(somme):
    if somme in solutions:
        return solutions[somme]
    if somme in liste_valeurs:
        solutions[somme] = 1
    else:
        solutions[somme] = 1 + min(rendu_rec_dyn(somme - piece) for piece in liste_valeurs if piece < somme)
    return solutions[somme]


def rendu_rec_dyn_liste(somme) -> list:
    if somme in solutions:
        return solutions[somme]
    if somme in liste_valeurs:
        solutions[somme] = [somme]
    else:
        liste_sous_problemes = []
        for piece in liste_valeurs:
            if piece < somme:
                liste_sous_problemes.append((piece, rendu_rec_dyn_liste(somme - piece)))
        choix = min(liste_sous_problemes, key=lambda x: len(x[1]))
        solutions[somme] = [choix[0]] + choix[1]
    return solutions[somme]


def goldbach(somme) -> list:
    if somme in solutions:
        return solutions[somme]
    if somme in liste_valeurs:
        solutions[somme] = [somme]

    else:
        liste_sous_problemes = []
        for piece in liste_valeurs:
            if piece < somme:
                liste_sous_problemes.append((piece, goldbach(somme - piece)))
        if liste_sous_problemes:
            choix = min(liste_sous_problemes, key=lambda x: len(x[1]))
            solutions[somme] = [choix[0]] + choix[1]
        else:
            return []

    return solutions[somme]


def rendu_glouton_liste(montant: int) -> list:
    liste_rendu = []
    while montant > 0:
        i = 0
        while liste_valeurs[i] > montant:
            i += 1
        liste_rendu.append(liste_valeurs[i])
        montant -= liste_valeurs[i]
    return liste_rendu


liste_valeurs = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
liste_valeurs.reverse()
solutions = dict()

for i in range(2, 50):
    print(i, goldbach(i))
