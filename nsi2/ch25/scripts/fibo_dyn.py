solution = [1, 1]  # on sait que les 2 premiers termes sont 1


def fibo_dyn(n):
    if n >= len(solution):  # si solution[n] n'existe pas
        r = fibo_dyn(n - 1) + fibo_dyn(n - 2)  # on calcule récursivement
        solution.append(r)  # puis on stocke la solution
        return r  # et on la renvoie
    else:
        return solution[n]  # sinon on renvoie la solution déjà calculée

print(fibo_dyn(500))