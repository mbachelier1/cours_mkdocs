dico_dyn = dict()  # Pour stocker les factorielles


def factorielle(n: int) -> int:  # version dynamique
	if n in dico_dyn:
		return dico_dyn[n]
	elif n == 0:
		dico_dyn[1] = 1
		return 1
	else:
		r = n * factorielle(n - 1)
		dico_dyn[n] = r
		return r


def approx_e(n):
	return sum(1 / factorielle(k) for k in range(n, -1, -1))  # règle de la photo de classe !


def decimales_de_e(n: int) -> float:
	a = 1  # 1ere somme partielle, pour i == 0
	b = 2  # pour i == 1
	i = 2  # ainsi i == 2
	while b - a > 10 ** (-n):  # tant qu'on n'a pas la précision souhaitée
		a, b = b, approx_e(i)  # on itère
		i = i + 1
	return round(b, n)  # on renvoie le résultat tronqué à n décimales

print(decimales_de_e(5))
