liste_valeurs = [500, 200, 100, 50, 20, 10, 5, 2, 1]


def rendu_monnaie(montant: int) -> list:
    liste_rendu = []
    while montant > 0:
        i = 0
        while liste_valeurs[i] > montant:
            i += 1
        liste_rendu.append(liste_valeurs[i])
        montant -= liste_valeurs[i]
    return liste_rendu
